# # importing scikit learn with make_blobs
# import numpy as np
# import matplotlib.pyplot as plt
# # from sklearn import svm
# import pandas as pd
# from matplotlib import style
# style.use("ggplot")
# import csv
# import json
# from sklearn.svm import SVR
# svr = SVR(kernel="linear",gamma="auto")
#
#
# # go through both files and find dissimilar longitude and latitude
#
# headers = ['TimeUS', 'Roll', 'Pitch', 'Yaw', 'Alt', 'Lat', 'Lng', 'Q1', 'Q2', 'Q3', 'Q4']
#
#
# class TestCsv:
#
#     def __init__(self):
#         self.true_lat_list = []
#         self.true_lng_list = []
#         self.false_lat_list = []
#         self.false_lng_list = []
#
#
#     def open_file_w_headers(self):
#
#         with open('dataNTPath.csv') as f:
#             for line in csv.reader(f):
#
#                 self.true_lat_list.append(line[6])
#                 self.true_lng_list.append(line[7])
#         #         print('lat is' , line[6])
#         # print(len(self.true_lng_list))
#
#
#     def open_file_w_headers_second(self):
#
#         with open('dataNDetourR.csv') as f:
#             for line in csv.reader(f):
#
#                 self.false_lat_list.append(line[6])
#                 self.false_lng_list.append(line[7])
#         #         print('lat is' , line[6])
#         #
#         # print(len(self.false_lng_list))
#
#     def compare_lat_lng(self):
#
#
#         false_counter = 0
#         print(len(self.false_lng_list))
#         print(len(self.true_lng_list))
#
#         # for each_false in self.false_lng_list:
#         #     if each_false not in self.true_lng_list and each:
#         #         false_counter = false_counter + 1
#         # print(false_counter)
#
#         true_counter = 0
#         for i in range(len(self.false_lng_list)):
#             if self.false_lng_list[i] in self.true_lng_list:
#                 ind = self.true_lng_list.index(self.false_lng_list[i])
#                 if self.false_lat_list[i] in self.true_lat_list[ind]:
#                     true_counter = true_counter + 1
#         print(true_counter)
#
#
# def main():
#     obj = TestCsv()
#     obj.open_file_w_headers()
#     obj.open_file_w_headers_second()
#     obj.compare_lat_lng()
#
# if __name__ == '__main__': main()
# #print(open_file_w_headers_second())



from matplotlib import style

style.use("ggplot")
import csv
from sklearn.svm import SVR

svr = SVR(kernel="linear", gamma="auto")

# go through both files and find dissimilar longitude and latitude

headers = ['TimeUS', 'Roll', 'Pitch', 'Yaw', 'Alt', 'Lat', 'Lng', 'Q1', 'Q2', 'Q3', 'Q4']


class TestCsv:

    def __init__(self):
        self.true_lat_list = []
        self.true_lng_list = []
        self.false_lat_list = []
        self.false_lng_list = []

    #true
    def open_file_w_headers(self):

        with open('dataNW-Truepath3.csv') as f:
            next(f)
            for line in csv.reader(f):
                line[6] = '{:011.5f}'.format(round(float(line[6]), 5))
                line[7] = '{:011.5f}'.format(round(float(line[7]), 5))
                if line[6] not in self.true_lat_list:
                    self.true_lat_list.append(line[6])
                if line[7] not in self.true_lng_list:
                    self.true_lng_list.append(line[7])

    #detour
    def open_file_w_headers_second(self):

        false_counter = 0
        compared_file_list = []
        first_line = ['Start', 'TimeUS', 'Roll', 'Pitch', 'Yaw', 'Alt', 'Lat', 'Lng', 'Q1', 'Q2', 'Q3', 'Q4',
                      'Category']
        with open('dataNW-DetourR3.csv') as f:
            next(f)
            for line in csv.reader(f):
                current_line = line
                line[6] = '{:011.5f}'.format(round(float(line[6]), 5))
                line[7] = '{:011.5f}'.format(round(float(line[7]), 5))
                if line[6] not in self.true_lat_list or line[7] not in self.true_lng_list:
                    false_counter += 1
                    current_line.append(1)
                    compared_file_list.append(current_line)
                else:
                    current_line.append(0)
                    compared_file_list.append(current_line)
        f.close()

        with open('comparedNW.csv', 'w', newline='') as openFile:
            writer = csv.writer(openFile)
            writer.writerow(first_line)
            for row in compared_file_list:
                writer.writerow(row)

        openFile.close()

    def check_category(self):
        cat_list = []
        with open('comparedNW.csv') as f:
            for line in csv.reader(f):
                print(line[12])
                if line[12] == '1':
                    cat_list.append(line[12])
        print('predicted number of incorrect values is' , len(cat_list))
        print('actual number of incorrect values is 1096')

def main():
    obj = TestCsv()
    obj.open_file_w_headers()
    obj.open_file_w_headers_second()
    # obj.compare_lat_lng()
    obj.check_category()


if __name__ == '__main__': main()

#272