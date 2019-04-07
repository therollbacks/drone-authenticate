import os
from matplotlib import style
import csv
from sklearn.svm import SVR
from numpy import linspace

style.use("ggplot")

svr = SVR(kernel="linear", gamma="auto")

# go through both files and find dissimilar longitude and latitude

headers = ['TimeUS', 'Roll', 'Pitch', 'Yaw', 'Alt', 'Lat', 'Lng', 'Q1', 'Q2', 'Q3', 'Q4']
first_line = ['Start', 'TimeUS', 'Roll', 'Pitch', 'Yaw', 'Alt', 'Lat', 'Lng', 'Q1', 'Q2', 'Q3', 'Q4',
              'Category']
full_data = []
sample_size = 100000


class TestCsv:

    def __init__(self):
        self.true_lat_list = []
        self.true_lng_list = []
        self.true_roll_list = []
        self.true_pitch_list = []
        self.true_yaw_list = []
        self.false_lat_list = []
        self.false_lng_list = []
        self.lat_min = 0
        self.lng_min = 0
        self.lat_max = 0
        self.lng_max = 0

    # true
    def open_file_w_headers(self, goodfile, badfile, justname):

        self.true_lat_list = []
        self.true_lng_list = []
        self.true_roll_list = []
        self.true_pitch_list = []
        self.true_yaw_list = []
        self.false_lat_list = []
        self.false_lng_list = []
        self.lat_min = 0
        self.lng_min = 0
        self.lat_max = 0
        self.lng_max = 0

        with open(goodfile) as f:
            print("goodfile is ", goodfile)
            next(f)
            for line in csv.reader(f):
                if line[6] not in self.true_lat_list:
                    self.true_lat_list.append(float(line[6]))
                if line[7] not in self.true_lng_list:
                    self.true_lng_list.append(float(line[7]))

        error_range = 0.0000100
        self.lat_min = min(self.true_lat_list) - error_range
        self.lat_max = max(self.true_lat_list) + error_range
        self.lng_min = min(self.true_lng_list) - error_range
        self.lng_max = max(self.true_lng_list) + error_range

        print(self.lat_min, self.lat_max)
        print(self.lng_min, self.lng_max)

        self.open_file_w_headers_second(badfile, justname)

    # detour
    def open_file_w_headers_second(self, badfile, justname):
        false_counter = 0
        compared_file_list = []
        with open(badfile) as f:
            next(f)
            for line in csv.reader(f):
                current_line = line
                if float(line[6]) < self.lat_min or float(line[6]) > self.lat_max:
                    false_counter += 1
                    current_line.append(1)
                    compared_file_list.append(current_line)
                elif float(line[7]) < self.lng_min or float(line[7]) > self.lng_max:
                    false_counter += 1
                    current_line.append(1)
                    compared_file_list.append(current_line)
                else:
                    current_line.append(0)
                    compared_file_list.append(current_line)
        f.close()

        print(false_counter)

        compared_file_name = 'compared' + justname + '.csv'
        with open(compared_file_name, 'w', newline='') as openFile:
            print('making compare file')
            writer = csv.writer(openFile)
            writer.writerow(first_line)
            for row in compared_file_list:
                writer.writerow(row)

        for row in compared_file_list:
            row.append(justname)
            full_data.append(row)
        openFile.close()

    def check_category(self):
        cat_list = []
        with open('comparedNW.csv') as f:
            for line in csv.reader(f):
                print(line[12])
                if line[12] == '1':
                    cat_list.append(line[12])
        print('predicted number of incorrect values is', len(cat_list))
        print('actual number of incorrect values is 1096')


def main():
    obj = TestCsv()
    # obj.open_file_w_headers_second()

    pathName = os.getcwd()

    goodFiles = []
    badFiles = []
    fileNames = os.listdir(pathName)

    for fileNames in fileNames:
        if fileNames.endswith("TP.csv"):
            goodFiles.append(fileNames)
        if fileNames.endswith("DT.csv"):
            badFiles.append(fileNames)

    goodFiles.sort()
    badFiles.sort()

    count = 0
    for i in range(0, len(goodFiles)):
        # print(goodFiles[i])
        # print(badFiles[i])
        good_data_file_name = goodFiles[i]
        bad_data_file_name = badFiles[i]
        if good_data_file_name[:-6] == bad_data_file_name[:-6]:
            print("checked ", good_data_file_name[:-6])
            obj.open_file_w_headers(goodFiles[i], badFiles[i], good_data_file_name[:-6])
            count = count + 1

        # if goodFiles[i].endswith('TP.csv'):
        #     url = good_data_file_name[:-6]
        #
        # compared_file_name = 'compared'+ data_file_name[0:7]
        # print(compared_file_name)

    with open("all_data.csv", 'w', newline='') as openFile:
        print('making final file')
        writer = csv.writer(openFile)
        writer.writerow(first_line)
        for row in full_data:
            writer.writerow(row)


if __name__ == '__main__': main()

# 272
