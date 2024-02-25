#Kosullu durumlar 
# If, Elif, Else



#If, Elif ve Else kullanimi örnek
E= "Erkek"
K = "Kadin "
D = "Diğer"


cinsiyet = str(input("Cinsiyetinizi Giriniz : Erkek E, kadin K, Diğer D"))
#Kosul olarak Eger cinsiyet = 1. secim ise
if cinsiyet.capitalize() == "E":
    print(E)
#Kosul olarak eger 1, degil 2. secim ise
elif cinsiyet.capitalize() == "K":
    print(K)
elif cinsiyet.capitalize() == "D":
    print(D)
#Kosul olarak secimler arasinda yoksa 
else:
    print("Gecersiz secim")



