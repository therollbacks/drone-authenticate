import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
data_list = []

class LogisticRegression:

    def __init__(self):
        self.algorithm()
        self.avg_acc_list = []

    def algorithm(self):
        data = np.loadtxt('./compared_auto_backup/cleandatagp4_010compared.csv', delimiter=",", skiprows=1)
        x = data[:, 4:6]
        y = data[:, 6]

        X = np.ones(shape=(x.shape[0], x.shape[1] + 1))
        X[:, 1:] = x

        initial_theta = np.zeros(X.shape[1])  # set initial model parameters to zero
        theta = opt.fmin_cg(self.cost, initial_theta, self.cost_gradient, (X, y))

        # x_axis = np.array([min(X[:, 1]) - 2, max(X[:, 1]) + 2])
        # y_axis = (-1 / theta[2]) * (theta[1] * x_axis + theta[0])
        # ax.plot(x_axis, y_axis, linewidth=2)

        predictions = np.zeros(len(y))
        predictions[self.sigmoid(X @ theta) >= 0.5] = 1
        self.avg_acc_list.append(np.mean(predictions == y) * 100)
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
    myavg = self.avg_acc_list
    print("Avg: ",)

if __name__ == '__main__':
    main()