from openpyxl import Workbook
wb = Workbook()
# The default sheet "Sheet" is already created.
# No need to add data for a blank spreadsheet.
wb.save("blank_spreadsheet.xlsx")
print("Blank Excel spreadsheet 'blank_spreadsheet.xlsx' created successfully.")