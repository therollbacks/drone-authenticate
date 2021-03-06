import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import matplotlib.pyplot as plt


class LogisticRegression:

    def __init__(self):
        self.algorithm()

    def algorithm(self):
        my_counter = 0
        # data = np.loadtxt('./compared_auto_backup/cleandatagp4_010compared.csv', delimiter=",", skiprows=1)
        for file in file_list:
            data = np.loadtxt('./compared_auto_backup/' + file, delimiter=",", skiprows=1)
            x = data[:, 4:6]
            y = data[:, 6]

            X = np.ones(shape=(x.shape[0], x.shape[1] + 1))
            X[:, 1:] = x

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

            initial_theta = np.zeros(X.shape[1])  # set initial model parameters to zero
            theta = opt.fmin_cg(self.cost, initial_theta,  self.cost_gradient, (X, y))

            # x_axis = np.array([min(X[:, 1]) - 2, max(X[:, 1]) + 2])
            # y_axis = (-1 / theta[2]) * (theta[1] * x_axis + theta[0])
            # ax.plot(x_axis, y_axis, linewidth=2)

            predictions = np.zeros(len(y))
            predictions[self.sigmoid(X @ theta) >= 0.5] = 1
            TP = FN = FP = TN = 0
            # print(len(y), len(predictions))
            for j in range(len(y)):
                if y[j] == 0 and predictions[j] == 1:
                    TP = TP + 1
                elif y[j] == 0 and predictions[j] == -1:
                    FN = FN + 1
                elif y[j] == 1 and predictions[j] == 1:
                    FP = FP + 1
                else:
                    TN = TN + 1
            # print(TP, FN, FP, TN)

            # Performance Matrix

            accuracy = (TP + TN) / (TP + FN + FP + TN)
            avg_acc_list2.append(accuracy)
            # print("accuracy:", accuracy)
            # sensitivity = TP / (TP + FN)
            # print(sensitivity)
            # avg_sens_list.append(sensitivity)
            specificity = TN / (TN + FP)
            avg_spec_list.append(specificity)
            predict = np.mean(predictions == y) * 100
            # Skip error data points
            if predict >= 5:
                avg_acc_list.append(predict)
            else: my_counter += 1
            # print("Training Accuracy =", str(np.mean(predictions == y) * 100) + "%")
        print("Average accuracy: ", sum(avg_acc_list) / len(avg_acc_list))
        print("Average accuracy2: ", sum(avg_acc_list2) / len(avg_acc_list2))
        print("Average specificity: ", sum(avg_spec_list) / len(avg_spec_list))
        # print("Average sensitivity: ", sum(avg_sens_list) / len(avg_sens_list))
        print("Median accuracy: ", statistics.median(avg_acc_list))

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
