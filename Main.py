dx = int(input("Введите шаг"))
x1 = -7
x2 = 11
while x1 + dx <= 11:
    x1 = x1 + dx
    if x1 + dx < -3:
        y = 3
        print(y)
    elif(x1 + dx > -3) & (x1 + dx <= 3):
        y = 3 + -((9-(x1)**2)**(1/2))
        print(y)
    elif(x1 + dx > 3) & (x1+ dx <= 6):
        y = -2*(x1-3)+3
        print(y)
    elif x1 + dx > 6:
        y = x1 - 9
        print(y)
