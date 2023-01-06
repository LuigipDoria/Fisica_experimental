import pandas as pd
import numpy as np
import math

#x1 = float(input("Digite o valor do x1 para o primeiro ponto: "))
#y1 = float(input("Digite o valor do y1 para o primeiro ponto: "))

#x2 = float(input("Digite o valor do x2 para o segundo ponto: "))
#y2 = float(input("Digite o valor do y2 para o segundo ponto: "))

# PARTE 1 VENDO OS PONTOS NO GRAFICO

data = pd.read_csv("fisica_exp.csv", sep=";")

data = data[["X", "Y"]]

predict = "Y"

X = np.array(data.drop(columns=predict))
y = np.array(data[predict])

lista_x = list(data["X"])
lista_y = list(data["Y"])

p1 = (lista_x[0], lista_y[0])
p2 = (lista_x[-1], lista_y[-1])

B = (math.log10(p2[1]/p1[1])/math.log10(p2[0]/p1[0]))

A = math.log10(p2[1])-B*math.log10(p2[0])

C = 10**A

print('B: ', B)
print('A: ', A)
print('C: ', C)


# PARTE 2 ESCOLHENDO O VALOR DE X PARA ACAHAR O Y PELA A FUNÇÃO A RETA

print('\nParte2\n')

x1 = float(input('X1: '))
y1 = float(input('Y1: '))
    
x2 = float(input("X2: "))
y2 = float(input("Y2: "))

B = (math.log10(y2/y1)/math.log10(x2/x1))

A = math.log10(y2)-B*math.log10(x2)

C = 10**A

print('B: ', B)
print('A: ', A)
print('C: ', C)
print('graviade',(2*math.pi/C)**2)