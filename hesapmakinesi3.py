#Hesap makinesi 3

S1 = int(input("Sayi : "))
i1 = input("İşlem : ")
S2 = int(input("Sayi : "))

T = (S1+S2)
C = (S1-S2)
B = (S1/S2)
X = (S1*S2)
NoktasizB = (S1//S2)

if i1 == "+":
    print("SOnuç : ", (T))

elif i1 == "-":
    print("Sonuç : ", (C))

#elif i1 == "/":
#    print("Sonuç : ", (B))
elif i1 == "*":
    print("Sonuç : ", (X))
elif i1 == "/":
    print("Sonuç : ", (B), ("VE"),  (NoktasizB))
else:
    print("Geçersiz işlem sirasi.")