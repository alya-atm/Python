#Функция суммы
def plus(x, y):
    sm = []
    k = 0
    if len(x) >= len(y):
        y = [0] * (len(x) - len(y)) + y
    elif len(x) < len(y):
        x = [0] * (len(y) - len(x)) + x
    x = x[::-1]
    y = y[::-1]
    for i, j in zip(x, y):
        if i + j + k >= 10:

            sm.append(i + j + k - 10)
            k = +1
        elif i + j < 10:
            sm.append(i + j + k)
            k = 0
    if k == 1:
        sm.append(k)
    sm=sm[::-1]
    return sm
#Вспомогательные функции для минимума
#Функция, когда x>y
def min1(x,y):
    mn=[]
    m=0
    x=x[::-1]
    y=y[::-1]
    for i, j in zip(y,x):
        if j-m>=i:
            mn.append(j-i-m)
            m=0
        elif j-m<i:
            mn.append(j+10-i-m)
            m=1
    mn=mn[::-1]
    return mn
#Функция, когда y>x
def min2(x,y):
    mn=[]
    m=0
    x=x[::-1]
    y=y[::-1]
    for i, j in zip(x,y):
        if j-m>=i:
            mn.append(j-i-m)
            m=0
        elif j-m<i:
            mn.append(j+10-i-m)
            m=1
    mn=mn[::-1]
    return mn

#Универсальная функция минимума
def minus(x, y):
    if len(x) > len(y):
        y = [0] * (len(x) - len(y)) + y
        return min1(x, y)
    elif len(x) < len(y):
        x = [0] * (len(y) - len(x)) + x
        return min2(x, y)
    if len(x) == len(y):
        for i, j in zip(x, y):
            if i > j:
                return min1(x, y)
                break
            elif i < j:
                return min2(x, y)
                break
            else:
                print(0)

x = [7,8,0]
y = [2,2,0]
x1=[8,4,5,0]
y1=[3,2,0]
x2=[1,1,5]
y2=[5,4,7,9]
print(plus(x,y))
print(plus(x1,y1))
print(plus(x2,y2))
print(minus(x,y))
print(minus(x1,y1))
print(minus(x2,y2))
