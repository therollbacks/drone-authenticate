import os
from matplotlib import style
import csv
from sklearn.svm import SVR
from numpy import linspace
import math

style.use("ggplot")

svr = SVR(kernel="linear", gamma="auto")

# go through both files and find dissimilar longitude and latitude

headers = ['Roll', 'Pitch', 'Yaw', 'Alt', 'Lat', 'Lng']
first_line = ['Roll', 'Pitch', 'Yaw', 'Alt', 'Lat', 'Lng', 'Category']
full_data = []
sample_size = 100000
filename_list = []


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
            print("badfile is ", badfile)

            next(f)
            for line in csv.reader(f):
                true_lat = format(float(line[4]), '.5f')
                true_lng = format(float(line[5]), '.5f')
                true_roll = format(float(line[0]), '.1f')
                true_pitch = format(float(line[1]), '.1f')
                true_yaw = round(float(line[2]))

                if true_lat not in self.true_lat_list:
                    self.true_lat_list.append(true_lat)
                if true_lng not in self.true_lng_list:
                    self.true_lng_list.append(true_lng)
                if true_yaw not in self.true_yaw_list:
                    self.true_yaw_list.append(true_yaw)

                if true_roll not in self.true_roll_list:
                    self.true_roll_list.append(true_roll)
                if true_pitch not in self.true_pitch_list:
                    self.true_pitch_list.append(true_pitch)


        # error_range = 0.0000000
        # self.lat_min = min(self.true_lat_list) - error_range
        # self.lat_max = max(self.true_lat_list) + error_range
        # self.lng_min = min(self.true_lng_list) - error_range
        # self.lng_max = max(self.true_lng_list) + error_range

        # print(self.lat_min, self.lat_max)
        # print(self.lng_min, self.lng_max)
        print("true lat list is ", self.true_lat_list)
        self.open_file_w_headers_second(badfile, justname)

    # detour
    def open_file_w_headers_second(self, badfile, justname):
        false_counter = 0
        compared_file_list = []
        with open(badfile) as f:
            next(f)

            for line in csv.reader(f):
                current_line = line
                bad_lat = format(float(line[4]), '.5f')
                bad_lng = format(float(line[5]), '.5f')
                bad_yaw = round(float(line[2]))

                bad_roll = format(float(line[0]), '.1f')
                bad_pitch = format(float(line[1]), '.1f')
                if bad_lat not in self.true_lat_list:
                    false_counter += 1
                    current_line.append(1)
                    compared_file_list.append(current_line)

                elif bad_lng not in self.true_lng_list:
                    false_counter += 1
                    current_line.append(1)
                    compared_file_list.append(current_line)

                elif bad_roll not in self.true_roll_list:
                    if bad_pitch not in self.true_pitch_list:
                        if bad_yaw not in self.true_yaw_list:
                            false_counter += 1
                            current_line.append(1)
                            compared_file_list.append(current_line)
                else:
                    current_line.append(0)
                    compared_file_list.append(current_line)
        f.close()

        # print("false count: " + false_counter)
        # print("just name is " +  justname)

        compared_file_name = './compared_auto/' + justname[17:] + 'compared.csv'
        # print(compared_file_name)
        with open(compared_file_name, 'w', newline='') as openFile:
            # print('making compare file')
            writer = csv.writer(openFile)
            writer.writerow(first_line)
            for row in compared_file_list:
                writer.writerow(row)

        for row in compared_file_list:
            row.append(justname)
            full_data.append(row)
        openFile.close()

    # def check_category(self):
    #     cat_list = []
    #     with open('comparedNW.csv') as f:
    #         for line in csv.reader(f):
    #             print(line[6])
    #             if line[6] == '1':
    #                 cat_list.append(line[6])
    #     print('predicted number of incorrect values is', len(cat_list))
    #     print('actual number of incorrect values is 1096')


def main():
    obj = TestCsv()
    # obj.open_file_w_headers_second()

    goodFiles = []
    badFiles = []
    fileNames = os.listdir("./formatted_auto")
    # print(fileNames)

    for fileName in fileNames:
        if ("dp") in fileName:
            # print('filename is '+ fileName)
            badFiles.append("./formatted_auto/" + fileName)

        elif ("gp") in fileName:
            # print('filename is '+ fileName)
            goodFiles.append("./formatted_auto/" + fileName)


        #
        # if fileName.endswith("TP.csv"):
        #     goodFiles.append("./formatted/" + fileName)
        # if fileName.endswith("DT.csv"):
        #     badFiles.append("./formatted/" + fileName)

    goodFiles.sort()
    badFiles.sort()

    count = 0
    for i in range(0, len(goodFiles)):
        # print(len(goodFiles))
        good_data_file_name = goodFiles[i]
        bad_data_file_name = badFiles[i]
        if good_data_file_name[28:] == bad_data_file_name[28:]:
            print("good_data_file_name is ", good_data_file_name[28:], "bad_data_file_name ", bad_data_file_name[28:])
            obj.open_file_w_headers(goodFiles[i], badFiles[i], good_data_file_name[:-4])
            count = count + 1

    # with open("all_data.csv", 'w', newline='') as openFile:
    #     print('making final file')
    #     writer = csv.writer(openFile)
    #     writer.writerow(first_line)
    #     for row in full_data:
    #         writer.writerow(row)


if __name__ == '__main__': main()

# 272
