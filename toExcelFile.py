import csv
import xlwt, xlrd
from xlutils.copy import copy as xl_copy


def csv_to_xlsx(csv_file, sheet_name):
	with open('000300.csv', 'r') as f:
		read = csv.reader(f)
		#workbook = xlwt.Workbook()
		# sheet = workbook.add_sheet('000300')
		
		rb = xlrd.open_workbook('history_data.xlsx', formatting_info=True)
		wb = xl_copy(rb)
		sheet = wb.add_sheet('data')
		
		l = 0
		for line in read:
			print(line)
			r = 0
			for i in line:
				print(i)
				sheet.write(l, r, i)
				r = r + 1
			l = l + 1

		#workbook.save('history_data.xlsx')
		wb.save('history_data.xlsx')



if __name__ == '__main__':
	csv_file = '000300.csv'
	sheet_name = '000300'
	csv_to_xlsx(csv_file, sheet_name)