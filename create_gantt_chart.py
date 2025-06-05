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
    phase_regex = re.compile(r"^\*\*Phase \d+: (.*?)(?:\s*\((Est\. Months \d+-\d+)\))?\*\*")
    # Regex to capture Activity lines like "1.  **Deep Dive into Existing UAT Processes & Test Assets**"
    activity_regex = re.compile(r"^(\d+\.)\s*\*\*(.*)\*\*")
    # Regex to capture Timeline lines like "*   **Timeline/Effort:** Weeks 1-3 (~10-12 person-days)"
    timeline_regex = re.compile(r"^\s*\*\s*Timeline/Effort:\s*(.*)")

    for line in md_text.splitlines():
        eng_match = engineer_regex.match(line)
        if eng_match:
            current_engineer = eng_match.group(1).strip()
            current_phase = None # Reset phase when engineer changes
            activities.append({"type": "engineer_header", "name": current_engineer})
            continue

        phase_match = phase_regex.match(line)
        if phase_match:
            phase_name_full = phase_match.group(1).strip()
            phase_timeline_est = phase_match.group(2) # This might be None
            current_phase = phase_name_full
            
            phase_timeline_str = ""
            if phase_timeline_est:
                # Extract just the "Months X-Y" part for the phase's own timeline bar
                month_part_match = re.search(r"Months (\d+-\d+)", phase_timeline_est, re.IGNORECASE)
                if month_part_match:
                    phase_timeline_str = f"Months {month_part_match.group(1)}"
            activities.append({"type": "phase_header", "name": current_phase, "engineer": current_engineer, "timeline_str": phase_timeline_str })
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
                "timeline_str": "" # Placeholder, will be filled by next line
            })
            continue
        
        timeline_match = timeline_regex.match(line)
        if timeline_match and activities and activities[-1]["type"] == "activity" and not activities[-1]["timeline_str"]:
            activities[-1]["timeline_str"] = timeline_match.group(1).strip()
            
    return activities

def parse_timeline_to_month_indices(timeline_str):
    months_touched_indices = set()
    
    month_range_match = re.search(r"Months (\d+)-(\d+)", timeline_str, re.IGNORECASE)
    if month_range_match:
        start_m_num = int(month_range_match.group(1))
        end_m_num = int(month_range_match.group(2))
        for m_idx in range(start_m_num - 1, end_m_num):
            if 0 <= m_idx < 6:
                months_touched_indices.add(m_idx)
        return sorted(list(months_touched_indices))

    week_match = re.search(r"Weeks (\d+)-(\d+)", timeline_str, re.IGNORECASE)
    if week_match:
        start_week = int(week_match.group(1))
        end_week = int(week_match.group(2))
        
        start_m = (start_week - 1) // 4 
        end_m = (end_week - 1) // 4
        
        for m_idx in range(start_m, end_m + 1):
            if 0 <= m_idx < 6:
                months_touched_indices.add(m_idx)
        return sorted(list(months_touched_indices))
        
    return sorted(list(months_touched_indices))


def create_gantt_excel(activities_data, filename="pilot_gantt_chart.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Pilot Gantt Chart"

    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
    activity_fill = PatternFill(start_color="B4C6E7", end_color="B4C6E7", fill_type="solid")
    engineer_header_fill = PatternFill(start_color="C0504D", end_color="C0504D", fill_type="solid")
    phase_header_fill = PatternFill(start_color="9BBB59", end_color="9BBB59", fill_type="solid")

    months = ["June (M1)", "July (M2)", "August (M3)", "September (M4)", "October (M5)", "November (M6)"]
    
    ws.cell(row=1, column=1, value="Activity / Task").font = header_font
    ws.cell(row=1, column=1).fill = header_fill
    ws.column_dimensions[get_column_letter(1)].width = 80
    for col_num, month_name in enumerate(months, 2):
        cell = ws.cell(row=1, column=col_num, value=month_name)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center")
        ws.column_dimensions[get_column_letter(col_num)].width = 18

    current_row = 2
    for item in activities_data:
        if item["type"] == "engineer_header":
            cell = ws.cell(row=current_row, column=1, value=item["name"])
            cell.font = Font(bold=True, size=14, color="FFFFFF")
            cell.fill = engineer_header_fill
            ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=len(months)+1)
            cell.alignment = Alignment(horizontal="center")
            current_row += 1
        elif item["type"] == "phase_header":
            cell = ws.cell(row=current_row, column=1, value=item["name"])
            cell.font = Font(bold=True, size=12, color="000000")
            cell.fill = phase_header_fill
            ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=1)
            month_indices_for_phase = parse_timeline_to_month_indices(item.get("timeline_str", ""))
            for m_idx in month_indices_for_phase:
                 col_to_color = m_idx + 2
                 ws.cell(row=current_row, column=col_to_color).fill = phase_header_fill # Use phase color for phase bar
            current_row += 1
        elif item["type"] == "activity":
            activity_display_name = f"{item['activity_num']} {item['name']}"
            name_cell = ws.cell(row=current_row, column=1, value=activity_display_name)
            name_cell.alignment = Alignment(wrap_text=True, vertical="top", indent=1)
            
            month_indices_to_color = parse_timeline_to_month_indices(item["timeline_str"])
            for m_idx in month_indices_to_color:
                col_to_color = m_idx + 2
                ws.cell(row=current_row, column=col_to_color).fill = activity_fill
            current_row += 1
    
    ws.row_dimensions[1].height = 20
    ws.freeze_panes = 'B2'

    wb.save(filename)
    print(f"Gantt chart '{filename}' created successfully.")

if __name__ == "__main__":
    markdown_file_path = "pilot_engineer_activities.md"
    try:
        with open(markdown_file_path, "r", encoding="utf-8") as f:
            markdown_file_content = f.read()
        activities_data_from_file = parse_markdown_for_gantt(markdown_file_content)
        if not activities_data_from_file:
            print(f"Warning: No activities parsed from {markdown_file_path}. Gantt chart might be empty or incorrect.")
        else:
            print(f"Successfully parsed {len(activities_data_from_file)} items from {markdown_file_path}.")
        create_gantt_excel(activities_data_from_file)
    except FileNotFoundError:
        print(f"ERROR: {markdown_file_path} not found. Cannot generate Gantt chart.")
    except Exception as e:
        print(f"An error occurred: {e}")
