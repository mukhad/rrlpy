import xlsxwriter
import csv


def write_csv(filename, data):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        num = 1
        for i in data:
            writer.writerow([num,i[0],i[1]])
            num += 1


def write_excel(filename, data):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
# Iterate over the data and write it out row by row.
    headers = ['0','path','file','Fd kHz','Fg kHz','Start','End','cnt','Source name']
    for h in headers:
        worksheet.write(row, col, h)
        col += 1

    row += 1
    col = 0
    num = 1

    for item in data:
        worksheet.write(row, col, num )
        worksheet.write(row, col + 1, item[0])
        worksheet.write(row, col + 2, item[1])
        worksheet.write(row, col + 3, "3180")
        row += 1
        num += 1
    workbook.close()

# Write a total using a formula.
# worksheet.write(row, 0, 'Total')
# worksheet.write(row, 1, '=SUM(B1:B4)')


