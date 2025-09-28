mn=int(input("Введите кол-во прошедших минут:"))
ch=0
while mn>=60:
    ch+=1
  mn-=60

while ch>=24:
    ch-=24


print(ch,"Часов",mn,"Минут")
