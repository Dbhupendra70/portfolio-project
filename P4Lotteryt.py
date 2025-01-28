import random
import matplotlib.pyplot as plt

times = int(input("for How many times you want to play: "))
account = 0
x =[]
y = []

for i in range(times):
    x.append(i+1)
    
    bet = int(input("Make your bet in between 1 to 10: "))
    lucky_draw = random.randint(1,10)
    
    print(f"Bet:{bet}\nLucky draw:{lucky_draw}")
    
    if bet == lucky_draw:
        # i will get 900(if won), spend 100 each time to partipate
        print("Congratulation! You won the bet :)")
        account = account+900-100
    else:
        print("Sorry! You lost :( ")
        account= account-100
    
    y.append(account)

print(" Final Amount in your game account: ",account)

chartDecision = input("if you want chart say y for yes: ")
if chartDecision == "y":
    plt.plot(x,y)
    plt.show()

                    