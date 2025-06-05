import re
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment
from openpyxl.utils import get_column_letter

# Note: This script expects 'pilot_engineer_activities.md' to be in the same directory.

def parse_markdown_for_gantt(md_text):
    activities = []
    current_engineer = None
    current_phase = None
    # Regex to capture Engineer lines like "## Engineer 1: Central UAT Test Case Identification & Migration"
    engineer_regex = re.compile(r"^## (Engineer \d+:.*)")
    # Regex to capture Phase lines like "**Phase 1: Discovery, Analysis & Planning (Est. Months 1-2)**"
    phase_regex = re.compile(r"^\*\*Phase \d+: (.*?)(?:\s*\((?:Est\.|Estimated)?\s*Months\s*\d+-\d+\))?\*\*")
    # Regex to capture Activity lines like "1.  **Deep Dive into Existing UAT Processes & Test Assets**"
    activity_regex = re.compile(r"^(\d+\.)\s*\*\*(.*)\*\*")
    # Regex to capture Timeline lines like "*   **Timeline/Effort:** Weeks 1-3 (~10-12 person-days)"
    # This regex now correctly captures the full 'Weeks X-Y...' string and the start/end week numbers
    timeline_regex = re.compile(r"^\s*\*\s*Timeline/Effort:\s*(Weeks\s*(\d+)-(\d+).*)")

    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        eng_match = engineer_regex.match(line)
        if eng_match:
            current_engineer = eng_match.group(1).strip()
            current_phase = None 
            activities.append({"type": "engineer_header", "name": current_engineer})
            i += 1
            continue

        phase_match = phase_regex.match(line)
        if phase_match:
            phase_name_full = phase_match.group(1).strip()
            current_phase = phase_name_full
            activities.append({"type": "phase_header", "name": current_phase, "engineer": current_engineer })
            i += 1
            continue
        
        activity_match = activity_regex.match(line)
        if activity_match:
            activity_num = activity_match.group(1)
            activity_name = activity_match.group(2).strip()
            
            # Look ahead for the timeline string for this activity
            timeline_raw_str = ""
            week_str_display = ""
            if i + 2 < len(lines): # Check there are enough lines for '* Activities:' and then '* Timeline/Effort:' or just '* Timeline/Effort'
                # Skip '* Activities:' line if present
                next_line_idx = i + 1
                if lines[next_line_idx].strip().startswith("*   **Activities:**"):
                    next_line_idx +=1 # Actual timeline is after this one
                
                # Now check the line at next_line_idx (or i + 1 if no Activities line)
                if next_line_idx < len(lines):
                    potential_timeline_line = lines[next_line_idx]
                    timeline_match_for_activity = timeline_regex.match(potential_timeline_line.strip()) # Strip leading spaces
                    if timeline_match_for_activity:
                        timeline_raw_str = timeline_match_for_activity.group(1).strip() # Full "Weeks X-Y..."
                        start_w = timeline_match_for_activity.group(2) # Start week number
                        end_w = timeline_match_for_activity.group(3)   # End week number
                        week_str_display = f"(W{start_w}-W{end_w})"

            activities.append({
                "type": "activity",
                "engineer": current_engineer,
                "phase": current_phase,
                "activity_num": activity_num,
                "name": activity_name,
                "timeline_raw_str": timeline_raw_str, 
                "week_str": week_str_display
            })
            i += 1 # Move to next line after activity name
            continue # Ensure we don't re-process this line
        
        i += 1 # Default increment if no match
            
    return activities

def parse_timeline_to_sprint_indices(timeline_raw_str, num_total_sprints=12):
    sprint_indices = set()
    if not timeline_raw_str: # Handle activities where timeline might not have been parsed
        return []
    
    week_match = re.search(r"Weeks\s*(\d+)-(\d+)", timeline_raw_str, re.IGNORECASE)
    if week_match:
        start_week = int(week_match.group(1))
        end_week = int(week_match.group(2))
        
        start_sprint = (start_week - 1) // 2 
        end_sprint = (end_week - 1) // 2   
        
        for sprint_idx in range(start_sprint, end_sprint + 1):
            if 0 <= sprint_idx < num_total_sprints:
                sprint_indices.add(sprint_idx)
        return sorted(list(sprint_indices))
        
    return sorted(list(sprint_indices))


def create_gantt_excel(activities_data, filename="pilot_gantt_chart.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Pilot Gantt (Sprints)"

    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
    activity_fill = PatternFill(start_color="B4C6E7", end_color="B4C6E7", fill_type="solid")
    engineer_header_fill = PatternFill(start_color="800000", end_color="800000", fill_type="solid") # Darker Red
    phase_header_fill = PatternFill(start_color="006400", end_color="006400", fill_type="solid") # Darker Green
    phase_font = Font(bold=True, size=12, color="FFFFFF")

    num_sprints = 12 
    sprint_headers = [f"Sprint {i+1} (W{2*i+1}-{2*i+2})" for i in range(num_sprints)]
    
    ws.cell(row=1, column=1, value="Activity / Task (Est. Timeline)").font = header_font
    ws.cell(row=1, column=1).fill = header_fill
    ws.column_dimensions[get_column_letter(1)].width = 95 # Activity Name column width expanded
    for col_num, sprint_name in enumerate(sprint_headers, 2):
        cell = ws.cell(row=1, column=col_num, value=sprint_name)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(col_num)].width = 15

    current_row = 2
    for item in activities_data:
        if item["type"] == "engineer_header":
            cell = ws.cell(row=current_row, column=1, value=item["name"])
            cell.font = Font(bold=True, size=14, color="FFFFFF")
            cell.fill = engineer_header_fill
            ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=len(sprint_headers)+1)
            cell.alignment = Alignment(horizontal="center", vertical="center")
            ws.row_dimensions[current_row].height = 20
            current_row += 1
        elif item["type"] == "phase_header":
            cell = ws.cell(row=current_row, column=1, value=item["name"])
            cell.font = phase_font
            cell.fill = phase_header_fill
            ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=len(sprint_headers)+1)
            cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
            ws.row_dimensions[current_row].height = 18
            current_row += 1
        elif item["type"] == "activity":
            activity_display_name = f"{item['activity_num']} {item['name']} {item.get('week_str', '')}"
            name_cell = ws.cell(row=current_row, column=1, value=activity_display_name)
            name_cell.alignment = Alignment(wrap_text=True, vertical="top", indent=2) 
            
            sprint_indices_to_color = parse_timeline_to_sprint_indices(item["timeline_raw_str"], num_sprints)
            for sprint_idx in sprint_indices_to_color:
                col_to_color = sprint_idx + 2 
                ws.cell(row=current_row, column=col_to_color).fill = activity_fill
            current_row += 1
    
    ws.row_dimensions[1].height = 40 
    ws.freeze_panes = 'B2'

    wb.save(filename)
    print(f"Gantt chart '{filename}' created successfully with sprint-based timelines and detailed activity display.")

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
        create_gantt_excel(activities_data_from_file, filename="pilot_gantt_chart_sprints.xlsx") # New filename
    except FileNotFoundError:
        print(f"ERROR: {markdown_file_path} not found. Cannot generate Gantt chart.")
    except Exception as e:
        print(f"An error occurred while generating Gantt chart: {e}")
        import traceback
        traceback.print_exc()
