import math

x1 = float(input("Digite o valor do x1 para o primeiro ponto: "))
y1 = float(input("Digite o valor do y1 para o primeiro ponto: "))

x2 = float(input("Digite o valor do x2 para o segundo ponto: "))
y2 = float(input("Digite o valor do y2 para o segundo ponto: "))


print('B: ',(math.log(y2)-math.log(y1))/(x2-x1))

print('A: ',-1/((math.log(y2)-math.log(y1))/(x2-x1)))

print('E0: ',math.log(y2)+(x2)/(-1/((math.log(y2)-math.log(y1))/(x2-x1))))

E0 = math.log(y2)+(x2)/(-1/((math.log(y2)-math.log(y1))/(x2-x1)))

print('E: ',math.e**(E0))