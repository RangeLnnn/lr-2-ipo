korzina=0
shkolnik=int(input("Введите количество школьников:"))
yabloki=int(input("Введите количетсво яблок:"))
kazhdomy=yabloki//shkolnik 
korzina = yabloki % shkolnik 
print(shkolnik,'школьникам достанется по',kazhdomy,'яблок каждому')
print(korzina,'яблок останется в корзине')  