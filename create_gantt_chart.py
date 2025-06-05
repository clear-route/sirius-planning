import re
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment
from openpyxl.utils import get_column_letter
import traceback

# Note: This script expects 'pilot_engineer_activities.md' to be in the same directory.

def parse_markdown_for_gantt(md_text):
    activities = []
    current_engineer = None
    current_phase = None
    
    engineer_regex = re.compile(r"^## (Engineer \d+:.*)")
    phase_regex = re.compile(r"^\*\*Phase \d+: (.*?)(?:\s*\((?:Est\.|Estimated)?\s*Months\s*\d+-\d+\))?\*\*")
    activity_regex = re.compile(r"^(\d+\.)\s*\*\*(.*)\*\*")
    # CORRECTED Regex for Timeline lines, accounting for markdown bold **Timeline/Effort:**
    timeline_capture_regex = re.compile(r"^\s*\*\s*\*\*Timeline/Effort:\*\*\s*(Weeks\s*(\d+)-(\d+).*)")

    lines = md_text.splitlines()
    
    for i, line in enumerate(lines):
        eng_match = engineer_regex.match(line)
        if eng_match:
            current_engineer = eng_match.group(1).strip()
            current_phase = None 
            activities.append({"type": "engineer_header", "name": current_engineer})
            continue

        phase_match = phase_regex.match(line)
        if phase_match:
            phase_name_full = phase_match.group(1).strip()
            current_phase = phase_name_full
            activities.append({"type": "phase_header", "name": current_phase, "engineer": current_engineer })
            continue
        
        activity_match = activity_regex.match(line)
        if activity_match:
            activity_num = activity_match.group(1)
            activity_name = activity_match.group(2).strip()
            
            timeline_raw_str = ""
            week_str_display = ""
            
            # Search for timeline in the next few lines following an activity
            for j in range(i + 1, min(i + 4, len(lines))): 
                current_line_for_timeline_check = lines[j]
                timeline_match_for_activity = timeline_capture_regex.match(current_line_for_timeline_check)
                if timeline_match_for_activity:
                    timeline_raw_str = timeline_match_for_activity.group(1).strip() 
                    start_w = timeline_match_for_activity.group(2) 
                    end_w = timeline_match_for_activity.group(3)   
                    week_str_display = f"(W{start_w}-W{end_w})"
                    break 
            
            activities.append({
                "type": "activity",
                "engineer": current_engineer,
                "phase": current_phase,
                "activity_num": activity_num,
                "name": activity_name,
                "timeline_raw_str": timeline_raw_str, 
                "week_str": week_str_display
            })
            continue
            
    return activities

def parse_timeline_to_sprint_indices(timeline_raw_str, num_total_sprints=12):
    sprint_indices = set()
    if not timeline_raw_str: 
        return []
    
    week_match = re.search(r"Weeks\s*(\d+)-(\d+)", timeline_raw_str, re.IGNORECASE)
    if week_match:
        try:
            start_week = int(week_match.group(1))
            end_week = int(week_match.group(2))
            
            start_sprint = (start_week - 1) // 2 
            end_sprint = (end_week - 1) // 2   
            
            for sprint_idx in range(start_sprint, end_sprint + 1):
                if 0 <= sprint_idx < num_total_sprints:
                    sprint_indices.add(sprint_idx)
            return sorted(list(sprint_indices))
        except ValueError:
            print(f"Warning: Could not parse week numbers from timeline string: {timeline_raw_str}")
            return []
        
    return sorted(list(sprint_indices))


def create_gantt_excel(activities_data, filename="pilot_gantt_chart_sprints.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Pilot Gantt (Sprints)"

    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid") # Blue
    activity_fill = PatternFill(start_color="B4C6E7", end_color="B4C6E7", fill_type="solid") # Light Blue
    engineer_header_fill = PatternFill(start_color="A52A2A", end_color="A52A2A", fill_type="solid") # Brown
    phase_header_fill = PatternFill(start_color="228B22", end_color="228B22", fill_type="solid") # Forest Green
    phase_font = Font(bold=True, size=12, color="FFFFFF")

    num_sprints = 12 
    sprint_headers = [f"Sprint {i+1} (W{2*i+1}-{2*i+2})" for i in range(num_sprints)]
    
    ws.cell(row=1, column=1, value="Activity / Task (Est. Timeline)").font = header_font
    ws.cell(row=1, column=1).fill = header_fill
    ws.column_dimensions[get_column_letter(1)].width = 100 

    for col_num, sprint_name in enumerate(sprint_headers, 2):
        cell = ws.cell(row=1, column=col_num, value=sprint_name)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(col_num)].width = 16

    current_row = 2
    activity_count = 0
    for item in activities_data:
        if item["type"] == "engineer_header":
            cell = ws.cell(row=current_row, column=1, value=item["name"])
            cell.font = Font(bold=True, size=14, color="FFFFFF")
            cell.fill = engineer_header_fill
            ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=len(sprint_headers)+1)
            cell.alignment = Alignment(horizontal="center", vertical="center")
            ws.row_dimensions[current_row].height = 22
            current_row += 1
        elif item["type"] == "phase_header":
            cell = ws.cell(row=current_row, column=1, value=item["name"])
            cell.font = phase_font
            cell.fill = phase_header_fill
            ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=len(sprint_headers)+1)
            cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
            ws.row_dimensions[current_row].height = 20
            current_row += 1
        elif item["type"] == "activity":
            activity_count += 1
            activity_display_name = f"{item['activity_num']} {item['name']} {item.get('week_str', '')}".strip()
            name_cell = ws.cell(row=current_row, column=1, value=activity_display_name)
            name_cell.alignment = Alignment(wrap_text=True, vertical="top", indent=2) 
            
            if not item["timeline_raw_str"]:
                print(f"Warning: Activity '{activity_display_name}' (parsed as item #{activity_count}) has no timeline_raw_str, skipping bar.")
            
            sprint_indices_to_color = parse_timeline_to_sprint_indices(item["timeline_raw_str"], num_sprints)
            if not sprint_indices_to_color and item["timeline_raw_str"]:
                 print(f"Debug: For activity '{activity_display_name}', timeline_raw_str '{item['timeline_raw_str']}' resulted in no sprint indices.")
            for sprint_idx in sprint_indices_to_color:
                col_to_color = sprint_idx + 2 
                ws.cell(row=current_row, column=col_to_color).fill = activity_fill
            current_row += 1
    
    ws.row_dimensions[1].height = 45 
    ws.freeze_panes = 'B2'

    try:
        wb.save(filename)
        print(f"Gantt chart '{filename}' created successfully with improved sprint-based timelines and activity details. Total activities processed for rows: {activity_count}")
    except Exception as e:
        print(f"Error saving Excel file '{filename}': {e}")
        traceback.print_exc()
    return activity_count # Return a value to check if activities were found

if __name__ == "__main__":
    markdown_file_path = "pilot_engineer_activities.md"
    print(f"Attempting to read markdown file: {markdown_file_path}")
    final_activity_count = 0
    try:
        with open(markdown_file_path, "r", encoding="utf-8") as f:
            markdown_file_content = f.read()
        print("Markdown file read successfully.")
        activities_data_from_file = parse_markdown_for_gantt(markdown_file_content)
        
        if not activities_data_from_file:
            print(f"Major Warning: NO activities were parsed from {markdown_file_path}. Gantt chart will likely be empty or incorrect.")
        else:
            parsed_activities_only = [item for item in activities_data_from_file if item['type'] == 'activity']
            print(f"Successfully parsed {len(activities_data_from_file)} total items (headers/activities); found {len(parsed_activities_only)} actual activity entries from {markdown_file_path}.")
        
        final_activity_count = create_gantt_excel(activities_data_from_file, filename="pilot_gantt_chart_sprints.xlsx")
        if final_activity_count == 0 and len(parsed_activities_only) > 0:
            print(f"CRITICAL WARNING: The script processed {len(parsed_activities_only)} parsed activities but wrote 0 activity rows to Excel. Check Excel generation logic.")
        elif final_activity_count > 0:
            print(f"Confirmed {final_activity_count} activity rows were written to Excel.")

    except FileNotFoundError:
        print(f"CRITICAL ERROR: Markdown file {markdown_file_path} not found. Cannot generate Gantt chart.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()
