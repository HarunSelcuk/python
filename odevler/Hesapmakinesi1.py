#Hesap Makinesi 1

A1 = int(input("Sayi Giriniz:"))
A2 = input("İşlem Giriniz (+,-,*,/)")
A3 = int(input("Sayi Giriniz:"))



Topla = A1+A3
cikar = A1-A3
carp = A1*A3
bol = A1/A3



if A2 =="+":
    print("Sonuç", Topla)
elif A2 =="-":
    print("Sonuç", (cikar))
elif A2 == "*":
    print("Sonuç", (carp))
elif A2 == "/":
    print("Sonuç", (bol))
else:
    print("Lütfen geçerli bir işlem seçiniz")
    A2 = input("İşlem Giriniz (+,-,*,/)")
    if A2 =="+":
        print("Sonuç", Topla)
    elif A2 == "-":
        print("Sonuç", (cikar))
    elif A2 == "/":
        print("Sonuç : ", (bol))
    elif A2 == "*":
        print("Sonuç", (carp))
    else:
        print("Şakire çay yok")
    


