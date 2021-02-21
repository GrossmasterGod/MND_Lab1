import random
M = 3
N = 8
X1,X2,X3 = [],[],[]
#Xn1,Xn2,Xn3 = [],[],[]
a0,a1,a2,a3 = 3,8,12,7
matrix = [[random.randrange(0,20) for y in range(M)] for x in range(N)]

for i in range(N):
    print(matrix[i])

Y = []
for i in range(len(matrix)):
    Y.append(a0+(a1*matrix[i][0])+(a2*matrix[i][1])+(a3*matrix[i][2]))
print(Y)
for i in range(len(matrix)):
    X1.append(matrix[i][0])
    X2.append(matrix[i][1])
    X3.append(matrix[i][2])

print("Ряди іксів:",X1,X2,X3)

x01 = (max(X1)+min(X1))/2
x02 = (max(X2)+min(X2))/2
x03 = (max(X3)+min(X3))/2
dx1 = x01 - min(X1)
dx2 = x02 - min(X2)
dx3 = x03 - min(X3)

lines = [X1,X2,X3]
Xn1 = [(X1[i]-x01)/dx1 for i in range(len(X1))]
Xn2 = [(X2[i]-x02)/dx2 for i in range(len(X2))]
Xn3 = [(X3[i]-x03)/dx3 for i in range(len(X3))]

print("Норм ікс 1:",Xn1)
print("Норм ікс 2:",Xn2)
print("Норм ікс 3:",Xn3)

Yet = a0+(a1*x01)+(a2*x02)+(a3*x03)
print("Еталон ігрик:",Yet)

check = Yet + max(Y)

for i in range(len(Y)):
    if abs(Yet - Y[i]) < check:
        check = abs(Yet - Y[i])
        wini = i
print(i)
print("Виграшний ряд:",matrix[i])

