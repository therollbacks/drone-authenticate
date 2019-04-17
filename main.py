from svm import SVM
from k_nearest import kNearest
import os


class Main:

    def __init__(self):
        print("starting ML models")
        self.pathName = os.getcwd()
        self.numFiles = []
        self.fileNames = os.listdir('compared_auto')
        self.k_nearest_model()

    # def svm_model(self):
    #
    #     svm_acc = []
    #     sum1 = 0
    #
    #     for filename in self.fileNames:
    #         sum = 0
    #         with open('compared_auto/' + filename) as f:
    #             for row in f:
    #                 sum = sum + 1
    #         obj_svm = SVM(filename, (sum * 0.75))
    #         res = obj_svm.model()
    #         svm_acc.append(res[4])
    #     for num in svm_acc:
    #         sum1 = sum1 + num
    #     avg_svm = sum1 / len(svm_acc)
    #     print('average svm is ', avg_svm)

    def k_nearest_model(self):
        trainingSet = []
        testSet = []
        split = 0.67
        k_acc = []
        sum1 = 0
        obj_k = kNearest()

        for filename in self.fileNames:
            sum = 0
            with open('k_auto/' + filename) as f:
                for row in f:
                    sum = sum + 1
            print("k-nearest for file ", filename)
            obj_k.loadDataset('./compared_auto/' + filename, split, trainingSet, testSet)
            print(('Train set: ' + repr(len(trainingSet))))
            print(('Test set: ' + repr(len(testSet))))
            # generate predictions
            predictions = []
            k = 3
            for x in range(len(testSet)):
                neighbors = obj_k.getNeighbors(trainingSet, testSet[x], k)
                result = obj_k.getResponse(neighbors)
                predictions.append(result)
                print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
            accuracy = obj_k.getAccuracy(testSet, predictions)
            print('Accuracy: ' + repr(accuracy) + '%')


if __name__ == '__main__': Main()
