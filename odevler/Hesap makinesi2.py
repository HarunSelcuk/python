Sayi1 = int(input("Sayi giriniz:"))
isaret = input("yapmak istediginiz islemi giriniz (+,-,*,/)=")
Sayi2 = int(input("Sayi giriniz:"))

Topla = (Sayi1+Sayi2)
cikar = (Sayi1-Sayi2)
carp = (Sayi1*Sayi2)
bol = (Sayi1/Sayi2)

if isaret =="+":
    print("Sonuç", (Topla))
elif isaret =="-":
    print("Sonuç", (cikar))
elif isaret == "*":
    print("Sonuç", (carp))
elif isaret == "/":
    print("Sonuç", (bol))
else:
    print("Geçerli bir sembol seçiniz.")