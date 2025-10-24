mn=int(input("Введите кол-во прошедших минут:"))
ch=mn//60
ost_mn=mn%60
ch=ch%24
print(ch,"Часов",ost_mn,"Минут")
