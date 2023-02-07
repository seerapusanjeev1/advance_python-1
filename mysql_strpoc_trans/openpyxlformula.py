from openpyxl.utils import FORMULAE
print(FORMULAE)
import openpyxl
from openpyxl.load_workbook("D://data//dataformula.xlsx")
sheet=wb.active
sheet["A7"]='SUM'(A1:A6)'
wb.save("d://data//newsheet.xlsx")