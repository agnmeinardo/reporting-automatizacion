import os
import glob
import csv
import xlwt # from http://www.python-excel.org/

for csvfile in glob.glob(os.path.join('.', '*')):
    print(csvfile)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('data')
    with open(csvfile, 'rt') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, val in enumerate(row):
                ws.write(r, c, val)
    os.remove(csvfile)
    wb.save(csvfile + '.xls')
