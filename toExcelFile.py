import csv
import xlwt, xlrd
from xlutils.copy import copy as xl_copy


def csv_to_xlsx(csv_file, sheet_name):
	print(csv_file)
	with open(csv_file, 'r') as f:
		read = csv.reader(f)
		#workbook = xlwt.Workbook()
		# sheet = workbook.add_sheet('000300')
		
		rb = xlrd.open_workbook('zhishu_history_data.xls')
		wb = xl_copy(rb)
		sheet = wb.add_sheet(sheet_name)
		
		l = 0
		for line in read:
			#print(line)
			r = 0
			for i in line:
				print(i)
				sheet.write(l, r, i)
				r = r + 1
			l = l + 1

		#workbook.save('history_data.xlsx')
		wb.save('zhishu_history_data.xls')



if __name__ == '__main__':
	csv_file = '399005.csv'
	sheet_name = '中小板指'
	csv_to_xlsx(csv_file, sheet_name)