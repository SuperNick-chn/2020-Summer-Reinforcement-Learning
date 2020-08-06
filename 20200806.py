# In this tutorial we are going to implement k-nearest neighbor search
# for a given toy data set in dimension two with labels 0 or 1

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

# We'll use the data set X where the first two entries are the x- and y-
# coordinate and the last entry is the label.

X = [[2.7810836, 2.550537003, -1],
     [1.465489372, 2.362125076, -1],
     [3.396561688, 4.400293529, -1],
     [1.38807019, 1.850220317, -1],
     [3.06407232, 3.005305973, -1],
     [7.627531214, 2.759262235, 1],
     [5.332441248, 2.088626775, 1],
     [6.922596716, 1.77106367, 1],
     [8.675418651, -0.242068655, 1],
     [7.673756466, 3.508563011, 1]]

# a will be an unlabeled point and we wish to determine if it
# should have label -1 (=red) or 1 (=blue). For now de put the label to
# -0.3(=yellow) to plot it in a color different from those appearing above

a = [4.4, 2.5, -0.3]

# Just for plotting we do the following (don't worry about this at the moment)
Y = np.append(np.array(X), np.array([a]), 0)


def euclidean_distance(vec1, vec2):
    sum = 0
    for i in range(len(vec1) - 1):
        sum = sum + (vec1[i] - vec2[i]) ** 2
    return sqrt(sum)


k = 1

# counter for red neighbors
c = 0

for j in range(1, k + 1):
    n = 0
    for i in range(len(X)):
        if euclidean_distance(a, X[n]) > euclidean_distance(a, X[i]):
            n = i
    if X[n][2] == -1:
        c = c + 1
    print(str(j) + "-th nearest neighbour is = " + str(X[n]))
    X.pop(n)

if c < 0.5 * k:
    print("New point should get blue label")
    Y[10][2] = 1
else:
    print("New point should get red label")
    Y[10][2] = -1

# This commands do the plotting

plt.scatter(Y[:, 0], Y[:, 1], s=50, c=Y[:, 2], cmap=plt.cm.Spectral)
plt.show()