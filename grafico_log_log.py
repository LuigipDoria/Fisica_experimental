import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle   
from matplotlib import style

# PARA FOLHA MONO-LOG

data = pd.read_csv("fisica_exp.csv", sep=";")

data = data[["X", "Y"]]

predict = "Y"

X = np.array(data.drop(columns=predict))
y = np.array(data[predict])


p = "X"
style.use("ggplot")
pyplot.scatter(data[p], data["Y"])      # PLOT DO PONTOS VERMELHOS
pyplot.loglog(X,y, "k")       # PLOT DA RETA FEITA PELA REGRESSÃO LINEAR
#pyplot.plot(X,y, "b*")      # PLOT DO P1 & P2
pyplot.xlabel("X")
pyplot.ylabel("Y")
pyplot.show()