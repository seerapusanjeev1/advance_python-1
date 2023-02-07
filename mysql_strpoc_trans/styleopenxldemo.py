from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sheet.title="Hcl"
sheet["A1"].value=10
sheet["B2"].value="test"
sheet.cell(row=3,column=3).value="Hcl data"
wb.save("..//data//demoopenxlwrite.xlsx")