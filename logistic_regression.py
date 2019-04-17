import csv

import numpy as np
import scipy.optimize as opt

data_list = []



class LogisticRegression:

    def __init__(self):
        x_list = []
        y_list = []
        with open('./compared_auto/cleandatagp2_009compared.csv') as f:
            next(f)
            for line in csv.reader(f):
                x_list = np.append(np.array([float(line[4]), float(line[5])]))
                y_list = np.append(float(line[6]))
        data = np.loadtxt('university_admission.txt', delimiter=",")
        print(type(data))
        x = x_list
        y = y_list
        print('got here')
        print(x, y)

        # fig, ax = plt.subplots()
        # positives = np.where(y == 1)
        # negatives = np.where(y == 0)
        # ax.scatter(x[positives, 0], x[positives, 1], marker="+", c='green')
        # ax.scatter(x[negatives, 0], x[negatives, 1], marker="x", c='red', linewidth=1)
        # plt.title("University Admission", fontsize=16)
        # plt.xlabel("exam 1 score", fontsize=14)
        # plt.ylabel("exam 2 score", fontsize=14)
        # plt.legend(["admitted", "not admitted"])
        # plt.show()

        X = np.ones(shape=(x.shape[0], x.shape[1] + 1))
        X[:, 1:] = x

        initial_theta = np.zeros(X.shape[1])  # set initial model parameters to zero
        theta = opt.fmin_cg(self.cost, initial_theta, self.cost_gradient, (X, y))

        # x_axis = np.array([min(X[:, 1]) - 2, max(X[:, 1]) + 2])
        # y_axis = (-1 / theta[2]) * (theta[1] * x_axis + theta[0])
        # ax.plot(x_axis, y_axis, linewidth=2)

        predictions = np.zeros(len(y))
        predictions[self.sigmoid(X @ theta) >= 0.5] = 1
        print("Training Accuracy =", str(np.mean(predictions == y) * 100) + "%")

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def cost(self, theta, X, y):
        predictions = self.sigmoid(X @ theta)
        predictions[predictions == 1] = 0.999  # log(1)=0 causes division error during optimization
        error = -y * np.log(predictions) - (1 - y) * np.log(1 - predictions);
        return sum(error) / len(y)

    def cost_gradient(self, theta, X, y):
        predictions = self.sigmoid(X @ theta)
        return X.transpose() @ (predictions - y) / len(y)


def main():
    mydata = LogisticRegression()
    print(mydata)


if __name__ == '__main__':
    main()
