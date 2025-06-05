import re
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment
from openpyxl.utils import get_column_letter

# Note: This script expects 'pilot_engineer_activities.md' to be in the same directory.

def parse_markdown_for_gantt(md_text):
    activities = []
    current_engineer = None
    current_phase = None
    engineer_regex = re.compile(r"^## (Engineer \d+:.*)")
    phase_regex = re.compile(r"^\*\*Phase \d+: (.*?)(?:\s*\((Est\. Months \d+-\d+)\))?\*\*")
    activity_regex = re.compile(r"^(\d+\.)\s*\*\*(.*)\*\*")
    timeline_regex = re.compile(r"^\s*\*\s*Timeline/Effort:\s*(Weeks (\d+)-(\d+).*)") # Capture week string and numbers

    for line in md_text.splitlines():
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
            activities.append({
                "type": "activity",
                "engineer": current_engineer,
                "phase": current_phase,
                "activity_num": activity_num,
                "name": activity_name,
                "timeline_raw_str": "", 
                "week_str": ""
            })
            continue
        
        timeline_match = timeline_regex.match(line)
        if timeline_match and activities and activities[-1]["type"] == "activity" and not activities[-1]["timeline_raw_str"]:
            activities[-1]["timeline_raw_str"] = timeline_match.group(1).strip()
            # Store Wx-y directly for display
            start_w = timeline_match.group(3)
            end_w = timeline_match.group(4)
            activities[-1]["week_str"] = f"(W{start_w}-{end_w})"
            
    return activities

def parse_timeline_to_sprint_indices(timeline_raw_str, num_total_sprints=12):
    sprint_indices = set()
    
    week_match = re.search(r"Weeks (\d+)-(\d+)", timeline_raw_str, re.IGNORECASE)
    if week_match:
        start_week = int(week_match.group(1))
        end_week = int(week_match.group(2))
        
        # Convert weeks to 0-indexed sprint numbers (2 weeks per sprint)
        start_sprint = (start_week - 1) // 2 
        end_sprint = (end_week - 1) // 2   
        
        for sprint_idx in range(start_sprint, end_sprint + 1):
            if 0 <= sprint_idx < num_total_sprints:
                sprint_indices.add(sprint_idx)
        return sorted(list(sprint_indices))
        
    return sorted(list(sprint_indices)) # Should always find Weeks for activities based on current MD structure


def create_gantt_excel(activities_data, filename="pilot_gantt_chart.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Pilot Gantt Chart (Sprints)"

    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
    activity_fill = PatternFill(start_color="B4C6E7", end_color="B4C6E7", fill_type="solid")
    engineer_header_fill = PatternFill(start_color="C0504D", end_color="C0504D", fill_type="solid")
    phase_header_fill = PatternFill(start_color="9BBB59", end_color="9BBB59", fill_type="solid")

    num_sprints = 12 # For a 6-month pilot (24 weeks)
    sprint_headers = [f"Sprint {i+1} (W{2*i+1}-{2*i+2})" for i in range(num_sprints)]
    
    ws.cell(row=1, column=1, value="Activity / Task (Timeline)").font = header_font
    ws.cell(row=1, column=1).fill = header_fill
    ws.column_dimensions[get_column_letter(1)].width = 90 # Activity Name column width
    for col_num, sprint_name in enumerate(sprint_headers, 2):
        cell = ws.cell(row=1, column=col_num, value=sprint_name)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(col_num)].width = 15

    current_row = 2
    for item in activities_data:
        if item["type"] == "engineer_header":
            cell = ws.cell(row=current_row, column=1, value=item["name"])
            cell.font = Font(bold=True, size=14, color="FFFFFF")
            cell.fill = engineer_header_fill
            ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=len(sprint_headers)+1)
            cell.alignment = Alignment(horizontal="center")
            current_row += 1
        elif item["type"] == "phase_header":
            cell = ws.cell(row=current_row, column=1, value=item["name"])
            cell.font = Font(bold=True, size=12, color="000000")
            cell.fill = phase_header_fill
            ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=len(sprint_headers)+1)
            cell.alignment = Alignment(horizontal="left", indent=1)
            current_row += 1
        elif item["type"] == "activity":
            # Include week string in the activity name display
            activity_display_name = f"{item['activity_num']} {item['name']} {item.get('week_str', '')}"
            name_cell = ws.cell(row=current_row, column=1, value=activity_display_name)
            name_cell.alignment = Alignment(wrap_text=True, vertical="top", indent=2) 
            
            sprint_indices_to_color = parse_timeline_to_sprint_indices(item["timeline_raw_str"], num_sprints)
            for sprint_idx in sprint_indices_to_color:
                col_to_color = sprint_idx + 2 # +2 because sprints start at col B (index 2)
                ws.cell(row=current_row, column=col_to_color).fill = activity_fill
            current_row += 1
    
    ws.row_dimensions[1].height = 30 # Adjusted for wrapped sprint headers
    ws.freeze_panes = 'B2'

    wb.save(filename)
    print(f"Gantt chart '{filename}' created successfully with sprint-based timelines.")

if __name__ == "__main__":
    markdown_file_path = "pilot_engineer_activities.md"
    try:
        with open(markdown_file_path, "r", encoding="utf-8") as f:
            markdown_file_content = f.read()
        activities_data_from_file = parse_markdown_for_gantt(markdown_file_content)
        if not activities_data_from_file:
            print(f"Warning: No activities parsed from {markdown_file_path}. Gantt might be empty.")
        else:
            print(f"Successfully parsed {len(activities_data_from_file)} items from {markdown_file_path}.")
        create_gantt_excel(activities_data_from_file)
    except FileNotFoundError:
        print(f"ERROR: {markdown_file_path} not found. Cannot generate Gantt chart.")
    except Exception as e:
        print(f"An error occurred while generating Gantt chart: {e}")
