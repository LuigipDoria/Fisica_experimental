import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle   
from matplotlib import style

potencia_x = 0
potencia_y = 0

############################################################################################################################################
################################################## NÃO MUDAR NADA ACIMA DESSA LINHA ########################################################
############################################################################################################################################

############################################################################################################################################
############################################################ INSTRUÇÕES ####################################################################
############################################################################################################################################

# OS VALORES DE X & Y DEVEM SER COLOCADOS NO ARQUIVO CHAMADO: fisica_exp.csv. OS VALORES DE X & Y JÁ TEM QUE ESTAR LINEARIZADOS
# OS VALORES DEVEM SER SEPARADOS POR PONTO E VIRGULA ( ; ) ONDE O NUMERO A ESQUERDA CORRESPONDE AO X E O NUMERO A DIREITA CORRESPONDE AO Y

# O GRAFICO GERADO NÃO ESTÁ NA ESCALA CALCULADA || TOMAR CUIDADO NA HORA DE PASSAR O GRAFICO PARA A FOLHA DE ENTREGA
# O GRAFICO COMEÇA NO PONTO X = 0 & Y = 0, TOMAR CUIDADO NISSO POIS PODE SER PEDIDO PARA NÃO COMEÇAR DO  PONTO X = 0 & Y = 0  
# OS PONTOS VERMELHOS SÃO OS PONTOS TABELADOS
# A RETA VERMELHA É A TENTATIVA DE SER A MELHOR RETA QUE PASSA POR TODOS OS PONTOS TABELADOS
# A RETA PRETA É FEITA ATRAVEZ DA REGRESSÃO LINEAR
# OS * EM AZUL SÃO OS PONTOS USADOS PARA GERAR UMA RETA A PARTIR DA FUNÇÃO FEITA PELA REGRESSÃO LINEAR

# PARA CASSO OS VALORES DE X E Y TENHA ALGUMA POTENCIA DE 10 TIRAR OS COMENTARIOS DAS PROXIMAS LINHAS E COLOCAR O EXPOENTE DA PONTECIA DE 10
# CASO NÃO TENHA POTENCIA DE 10 COMENTAR AS PROXIMAS LINHAS (PARA COMENTAR BASTA ADICIONAR UM # NO COMEÇO DA LINHA)

potencia_x = 0
potencia_y = 0

# FIM DA PARTE QUE PODE SER ALTERADA

# CASO QUEIRA ANALISAR ALGUMA INFORMAÇÃO EM ESPECIFICO DESCER ATÉ O FINAL DO CODIGO (contiua na linha de baixo)
# E COMENTAR AS LINHAS DAS INFORMAÇÕES QUE DESEJA TIRAR DO GRAFICO

###########################################################################################################################################
################################################## NÃO MUDAR NADA ABAIXO DESSA LINHA ######################################################
###########################################################################################################################################




data = pd.read_csv("fisica_exp.csv", sep=";")

data = data[["X", "Y"]]

predict = "Y"

X = np.array(data.drop(columns=predict))
y = np.array(data[predict])

# CALCULA A ESCALA

pe = [1,2,5,10,20,25,40,50,100,200,500,1000]

lista_x = list(data["X"])
lista_y = list(data["Y"])

x_inicial = lista_x[0]
x_final = lista_x[-1]

y_inicial = lista_y[0]
y_final = lista_y[-1]

escala_10 = (x_final-x_inicial)/18
escala_11 = (y_final-y_inicial)/28

escala_20 = (x_final-x_inicial)/28
escala_21 = (y_final-y_inicial)/18


def acha_escala(escala):
    i = 0 
    while pe[i]<escala:
        i += 1 
    return i

print()
print("Para a folha na VERTICAL")
print("Escala do eixo X:",pe[acha_escala(escala_10)])
print("Escala do eixo Y:",pe[acha_escala(escala_11)])
print()
print("Para a folha na HORIZONTAL")
print("Escala do eixo X:",pe[acha_escala(escala_20)])
print("Escala do eixo Y:",pe[acha_escala(escala_21)])

best = 0
for _ in range(30):

    linear = linear_model.LinearRegression()

    linear.fit(X, y)
    acc = linear.score(X, y)
    #print(acc)

    if acc> best:
        best = acc
        with open("fisica.pickle", "wb") as f:
            pickle.dump(linear, f)

print()
print("coeficiente de correlação: {:f}".format(acc))
pickle_in = open("fisica.pickle", "rb")
linear = pickle.load(pickle_in)

print("Valor do B:", linear.coef_[0])
print("Valor do A:",  linear.intercept_)
print("Valor da Gravidade: ", 2/linear.coef_[0])

A = linear.intercept_*10**potencia_y
B = linear.coef_[0]*10**potencia_y

A_r = round(linear.intercept_,3)*10**potencia_y
B_r = round(linear.coef_[0],3)*10**potencia_y

print()
print("A função é y = {} + {}*x".format(A_r, B_r))

print()
x1 = float(input("Digite o valor do x para o primeiro ponto: "))
x2 = float(input("Digite o valor do x para o segundo ponto: "))

y1 = round((A + B*x1)*10**abs(potencia_y),2)
y2 = round((A + B*x2)*10**abs(potencia_y),2)

print()
print("P1 -> (x = {} , y = {})".format(x1,y1))
print("P2 -> (x = {} , y = {})".format(x2,y2))


x_plot1 = np.array([lista_x[0],lista_x[-1]])
y_plot1 = np.array([lista_y[0],lista_y[-1]])

x_plot2 = np.array([x1,x2])
y_plot2 = np.array([y1,y2])

p = "X"
style.use("ggplot")
pyplot.scatter(data[p], data["Y"])      # PLOT DO PONTOS VERMELHOS
pyplot.plot(x_plot2,y_plot2, "k")       # PLOT DA RETA FEITA PELA REGRESSÃO LINEAR
pyplot.plot(x_plot1,y_plot1, "r-.")     # PLOT DA TENTIVA DA MELHOR RETA QUE PASSA POR TODOS OS PONTOS TABELADOS
pyplot.plot(x_plot2,y_plot2, "b*")      # PLOT DO P1 & P2
pyplot.xlabel("X")
pyplot.ylabel("Y")
pyplot.show()

