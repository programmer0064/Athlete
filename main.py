"""print("Hello World")
baslik = "Tasit kredisi"
print(baslik)
#string metinsel ifade
baslik = "Ihtiyac Kredisi"
print(baslik)

#int, integer => tam sayi
vade = 36
ekVade = 12
vade2 = "36"

#float, decimal, double
aylikOdeme = 200.50

#bool, boolean => True veya False
yukselisteMi = False

#matematiksel operatörler => alles nach demselben Prinzip
print(5 + 5 + vade + ekVade)

yeniVade = vade/2
fiyat= 100
inrimliFiyat = fiyat - 20

print(yeniVade)
print(inrimliFiyat)

#Control K control c for commenting
#% => mod operator
print(10%2)
print(vade % 3)
print(yeniVade % vade)

#mantiksal operatörler
print(1==1)
print(1==0)
print(3>1)
print(1>2)
print(1>=1)

print(1!=1)
print(1!=2)

#or and keywords operatorler
print(1>2 or 5>2) #or => veya
print(1>2 and 5>2) #and => ikiside true 
print(1>2 or 3>1 and 5>2)

#karar yapilari
#if else
sayi1=10
sayi2=15
print("********************************")
#sayi1 sayi2 den büyükse ekrana sayi1 daha büyük yazdir
#condition
if sayi1 > sayi2:
#indent
    print("sayi 1 " + "daha büyükdür")
    print("Hala if blogunun icerisindeyim")

elif sayi1==sayi2:
    print("iki sayi esittir")

else:
    print("sayi2 daha büyükdür")

print("Burasi if blogunun disidir") #true veya false yinede bu satiri görücez

"""
