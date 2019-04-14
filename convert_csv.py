from matplotlib import style

style.use("ggplot")
import csv
import json
import os
from sklearn.svm import SVR

svr = SVR(kernel="linear", gamma="auto")

headers = ['TimeUS', 'Roll', 'Pitch', 'Yaw', 'Alt', 'Lat', 'Lng', 'Q1', 'Q2', 'Q3', 'Q4']


class Format:
    def __init__(self):
        print("formatiing...")

    def open_file_w_headers(self, filedir, filename):
        counter = 0
        emp_list = []
        emp_list_inner = []
        with open(filedir) as f:
            for i in csv.reader(f):

                for each in i:

                    if ": SIM {" not in each:
                        if "}" in each:
                            each = each.rstrip("}")
                        # print("each is  " , each)
                        datarow = (each.split(':', 1)[-1])

                        emp_list_inner.append(datarow)
                        # print("datarow is ", datarow)
                    else:
                        cell2 = each.split(": SIM {TimeUS : ", 1)

                        for cell in cell2:
                            emp_list_inner.append(cell)

                emp_list.append(emp_list_inner)

                emp_list_inner = []
        new_file_name = "data" + filename

        with open('./formatted/' + new_file_name, 'w', newline='') as outfile:
            wr = csv.writer(outfile)
            wr.writerows(emp_list)

        with open('./formatted/' + new_file_name, newline='') as f:
            r = csv.reader(f)
            data = [line for line in r]

        with open('./formatted/' + new_file_name, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['Start', 'TimeUS', 'Roll', 'Pitch', 'Yaw', 'Alt', 'Lat', 'Lng', 'Q1', 'Q2', 'Q3', 'Q4'])
            w.writerows(data)




def main():
    obj = Format()

    pathName = os.getcwd()

    numFiles = []
    fileNames = os.listdir('unformatted')

    for fileNames in fileNames:
        if fileNames.endswith(".csv"):
            numFiles.append(fileNames)
    print(numFiles)

    count = 0
    for i in numFiles:
        filedir = (os.path.join(pathName, 'unformatted', i))

        obj.open_file_w_headers(filedir, numFiles[count])
        count = count + 1


if __name__ == '__main__': main()
