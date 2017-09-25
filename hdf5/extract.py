import csv
import xlrd
import xlsxwriter
# https://xlsxwriter.readthedocs.org/


def extract_info_from_excel(file_url):
    data = xlrd.open_workbook(file_url)
    table = data.sheet_by_index(0)
    for i in range(26):
        for j in range(2):
            print "i:" + str(i) + " j:" + str(j) + " =" + table.cell(j, i).value

            
extract_info_from_excel('Sample Planning Study Data_ESM_v4.xlsx')
