
x=float(input('Введите x:'))
y=float(input('Введите y:'))
f=(x**(y/x))-(pow(y/x,1/3))
if f<0:
    f*=-1
    
f=f+(y-x)
print("Значение функции будет примерно равно",(round(f,2)))