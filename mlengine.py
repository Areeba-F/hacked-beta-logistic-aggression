import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from PIL import Image

from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('\\wsl$\Ubuntu\home\backslash330\hack\database\thesocialnetwrok.csv')
x= dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

##print(x[0:5])
##print(' ')
##print(y[0:5])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.25, random_state = 42)

scx = StandardScaler()
xtrain = scx.fit_transform(xtrain)
xtest = scx.transform(xtest)

##print(xtrain[0:5])

##print(xtest[0:5])

cl = LogisticRegression(random_state=42)
cl.fit(xtrain, ytrain)

##print(cl.predict(scx.transform([[30,87000]])));

ypred = cl.predict(xtest)
concatenation = np.concatenate((ypred, ytest), 0)
concatenation = np.concatenate((ypred.reshape(len(ypred),1), ytest.reshape(len(ytest), 1)), 1)
##print(concatenation[0:20])

matr = confusion_matrix(ytest, ypred)
##print(matr)

##ConfusionMatrixDisplay(matr).plot()

accuracy_score(ytest, ypred)

