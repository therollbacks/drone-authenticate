from svm import SVM

import os

class Main:



    pathName = os.getcwd()
    numFiles = []
    fileNames = os.listdir('compared_auto')
    svm_acc = []
    sum1 = 0

    for filename in fileNames:
        sum = 0
        with open('compared_auto/' + filename) as f:
            for row in f:
                sum = sum + 1
        obj_svm = SVM(filename, (sum*0.75))
        res = obj_svm.model()
        svm_acc.append(res[4])
    for num in svm_acc:
        sum1 = sum1 + num
    avg_svm = sum1/len(svm_acc)
    print('average svm is ', avg_svm)



    count = 0

if __name__ == '__main__': Main()

