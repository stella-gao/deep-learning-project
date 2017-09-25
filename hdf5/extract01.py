import xlrd
workbook = xlrd.open_workbook('Sample Planning Study Data_ESM_v4.xlsx')
worksheet01 = workbook.sheet_by_name('Needs')
worksheet02 = workbook.sheet_by_name('Recommendations')

for i in range(1,56):
    with open('summary.txt', 'a') as f1:
        f1.write((worksheet01.cell(i, 3).value).encode('utf8'))
        f1.write("\n")

for j in range(1,237):
    with open('summary.txt', 'a') as f1:
        f1.write((worksheet02.cell(j, 3).value).encode('utf8'))
        f1.write("\n")
