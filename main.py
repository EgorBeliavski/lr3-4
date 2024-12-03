import math
a = int(input("Введите первый коофицент "))
b = int(input("Введите второй коофицент "))
c = int(input("Введите третий коофицент "))
D=(b*b)-(4*a*c)
if(D>0):
    x1 = (-b - math.sqrt(D))/(2*a)
    x2 = (-b + math.sqrt(D))/(2*a)
    print(x1,x2)
elif(D==0):
    x1= (-b)/2*a
else:
    print("Корней нет ")
