# def and While true:
# def ile daha sonra çagrılmak üzere işlem tanımlıyoruz. Böylece sürekli ayno kodu yazmaktan kurtuluyoruz.
# "While true: " ile kodun Döngüye girmesini saglıyoruz.

def weLcomepAge(): 
    print("Welcome")

def instructi(): 
    print(""" 
1-) Enter a number.
2-) Enter a math signs(+ , - . * , /).
3-) Enter a number again.
4-) see results.
          """)
#iişlem tanımlaamaları
def add( x,y):
    Result((x+y))
def sub(x,y):
    Result((x-y))
def mult(x,y):
    Result((x*y))
def divis(x,y):
    Result((x//y))


#Sonuç
def Result(op):              # Burada "OP" Neden kullanıldı ?
    print("Result : ", op)  

        
#Kullanıcının görüdüğü. 
def Mission():
    while True:
        try:
            
                
                s1 = int(input("Enter a number : "))
                s2 = input("Enter an math signs :")
                s3 = int(input("Enter another number :")) 

            

                if s2 == "+":
                    add(s1,s3)
                elif s2 =="-":
                    sub(s1,s3)
                elif s2 == "*":
                    mult(s1,s3)
                elif s2 == "/":
                    divis(s1,s3)
                else:    
                    print("""unknown signs.
Try again. """)
        except ZeroDivisionError:
            print("Result : 0")
        except ValueError:
            print("not a sign, just a number")

# Kodun çalışma sırası.

weLcomepAge()

instructi()

Mission()

    
