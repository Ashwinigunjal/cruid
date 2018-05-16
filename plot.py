import xlsxwriter

workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()

array = [4950,4950,500,1500,550,1500,500,500,500,1500,500,500,500,1500,500,500,500,1500,500,1500,500,1500,500,1500,550,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,500,500,1500,500,1500,500,1500,500,1500,500,1550,500,500,500,1500,500,500,500,500,500,1500,500,1500,500,1500,500,1550,500,1500,500,1500,500,1500,500,1500,500,1500,500,500,500,1500,500,1500,500,1500,500,500,500,550,500,1500,500,1500,500,1500,500,500,500,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,1500,550,1500,500,1500,500,1500,500,500,500,1500,500,500,500,1500,500,500,500,1550,500,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,500,500,1500,500,1500,500,1500,550,1500,500,1500,500,1500,500,1500,500,500,500,500,500,500,500,1500,500,1500,550,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,1500,500,550,500,1500,500,1500,500,500,500,1500,500,1500,500,1500,500,500,500,500,4950,
]

row = 0

for col, data in enumerate(array):
    worksheet.write_column(row, col, data)

workbook.close()