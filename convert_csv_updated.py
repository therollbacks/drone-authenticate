import csv
import json
import os
import pandas as pd
from sklearn.svm import SVR

headers = ['TimeUS', 'Roll', 'Pitch', 'Yaw', 'Alt', 'Lat', 'Lng', 'Q1', 'Q2', 'Q3', 'Q4']


class Format:
    def __init__(self):
        print("formating...")

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

        with open('./formatted_auto/' + new_file_name, 'w', newline='') as outfile:
            wr = csv.writer(outfile)
            wr.writerows(emp_list)

        with open('./formatted_auto/' + new_file_name, newline='') as f:
            r = csv.reader(f)
            data = [line for line in r]

        A = pd.read_csv(('./formatted_auto/' + new_file_name), names=headers)
        A.to_csv(('./formatted_auto/' + "new" + new_file_name), index=False)
        A_new = pd.read_csv('./formatted_auto/' + "new" + new_file_name)

        #convert yaw, roll pitch from radians to degree  Degree = radian * 180 / pi()

        data = A_new.drop(["TimeUS", "Q1", "Q2", "Q3", "Q4"], axis=1)
        data['Alt'] = data['Alt'].astype(float)
        data['Lat'] = data['Lat'].astype(float)
        data['Lng'] = data['Lng'].astype(float)
        data['Yaw'] = data['Yaw'].astype(float)
        data['Roll'] = data['Roll'].astype(float)
        data['Pitch'] = data['Pitch'].astype(float)
        data['Index'] = data.index

        data.to_csv(('./formatted_auto/' + "clean" + new_file_name), index=False)
        os.remove('./formatted_auto/' + new_file_name)
        os.remove('./formatted_auto/' + "new" + new_file_name)

        # Code to Reorder Columns
        #
        # with open('/formatted_auto/' + new_file_name, 'r') as infile, open('/reordered/' + new_file_name, 'a') as outfile:
        #     # output dict needs a list for new column ordering
        #     fieldnames = ['Index', 'Alt', 'Lat', 'Lng', 'Yaw','Pitch','Roll']
        #     writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        #     # reorder the header first
        #     writer.writeheader()
        #     for row in csv.DictReader(infile):
        #         # writes the reordered rows to the new file
        #         writer.writerow(row)


def main():
    obj = Format()

    pathName = os.getcwd()
    numFiles = []
    fileNames = os.listdir('unformatted_auto')

    for fileNames in fileNames:
        if fileNames.endswith(".csv"):
            numFiles.append(fileNames)
    count = 0
    for i in numFiles:
        filedir = (os.path.join(pathName, 'unformatted_auto', i))

        obj.open_file_w_headers(filedir, numFiles[count])
        count = count + 1

    # to confirm cleandata csv datatypes, uncomment
    # A = pd.read_csv(('./formatted/cleandataSet1DT.csv'))
    # print(A.dtypes)


if __name__ == '__main__': main()
