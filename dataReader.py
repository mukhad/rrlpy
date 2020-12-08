import os
import time


def files_sort(s):
    try:
        i = s.find(".")
        val = s[:i].split("_")[2]
    except:
        val = 0
        print(s)

    return int(val)


def readfilelist(datadir):
    d = os.listdir(datadir)
    rrlfiles = list()
    for dir in d:
        fn = os.path.join(datadir, dir)
        files = os.listdir(fn)
        files.sort(key=files_sort)

        for f in files:
            ff = (os.path.join(fn, f), f)
            rrlfiles.append(ff)



        # t = os.path.getmtime(fn)
        # s1 = time.strftime("%Y.%m.%d %H:%M", time.localtime(t))
        # print(fn, "\t", s1, "\t", len(files))

    return rrlfiles


'''
import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
'''

