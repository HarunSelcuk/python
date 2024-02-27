import random

def userinput():
    while True:
    
        Choice = input("Choice : ",).upper()  # Burada kalıyordum çünkü upperin sonuna () getirmedim :D
        if Choice in ('R', 'P', 'S'): 
            return Choice
        else:
            print("geçerisz giriş")

def Randompc():
    
    
    return random.choice(['R', 'P', 'S'])

def outcome(user,pc):
    if user==pc:
        return "DRAW"
    elif (user == "P" and pc == "R") or \
         (user == "S" and pc == "P") or \
         (user == "R" and pc == "S"):
        return "You Won"
    else:
        return "You Lost"


def game():
    score = 0
    hp = 5
    while hp>0:
        print("Welcome")
        print("Score : {}, HP : {}".format(score, hp))

        userturn = userinput() # bunu geçmiyor idi
        pcturn = Randompc()

        print("Pc Choice: ", pcturn)

        Resultate = outcome(userturn, pcturn)
        print(Resultate)
        if Resultate == "You Won":
            score += 5
        elif Resultate == "You Lost":
            hp -= 1

    print("Game over. Your total score : ", score)


game()





   
    
    











