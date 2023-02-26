import random, time
#rolling dice
def dice_roll(name):
    print("\n Its ", name, "time to roll the dice\n")
    input("Press enter to roll")
    time.sleep(1)
    print("...")
    time.sleep(1)
    dice1=random.randint(1,6)
    print(name, " rolled a ", dice1)
    dice_output(dice1)
    time.sleep(1)
    print("Dice 2 is being rolled")
    time.sleep(1)
    print("...")
    time.sleep(1)
    dice2=random.randint(1,6)
    print(name," rolled a ", dice2)
    dice_output(dice2)
    if dice1==dice2:
        print("Well done, you got a double, please roll again, press enter to roll")
        time.sleep(1)
        print("...")
        time.sleep(2)
        dice3=random.randint(1,6)
        dice_output(dice3)
        total=dice1+dice2+dice3
    else:
        total=dice1+dice2
    if total % 2==0:
        print("Congrats, you got a total score of ", total," which is even so you get 10 extra points")
        total+=10
    else:
        print("Unlucky you got a total score of ", total, "which is an odd number so you lose 5 points")
        total-=5
        if total<0:
            total=0
    print("\n", name, "You got a total of", total, "for this round\n")
    time.sleep(2)
    return total
    #outputting dice image 
def dice_output(dice):
    if dice==1:
        print(" ________ ")
        print("|        |")
        print("|   ()   |")
        print("|        |")
        print("|________|")
    if dice==2:
        print(" ________ ")
        print("|        |")
        print("|   ()   |")
        print("|        |")
        print("|   ()   |")
        print("|________|")
    if dice==3:
        print(" ________ ")
        print("|        |")
        print("|   ()   |")
        print("|        |")
        print("| ()  () |")
        print("|________|")
    if dice==4:
        print(" ________ ")
        print("|        |")
        print("| ()  () |")
        print("|        |")
        print("| ()  () |")
        print("|________|")
    if dice==5:
        print(" ________ ")
        print("|        |")
        print("| ()  () |")
        print("|   ()   |")
        print("| ()  () |")
        print("|________|")
    if dice==6:
        print(" ________ ")
        print("|        |")
        print("| ()  () |")
        print("| ()  () |")
        print("| ()  () |")
        print("|________|")
#playing the game
print("Welcome to the amazing dice game")
player1, player2="Mr Watts", "Mr Gordan"
player1total, player2total=0,0
for i in range(1,6):
    print("Round: ", i)
    player1total+=dice_roll(player1)
    player2total+=dice_roll(player2)
    print(player1," has a overall total of", player1total, "\n")
    print(player2, "has a overall total of", player2total, "\n")
#deciding the winner 
while player1total==player2total:
    print("Scores are tied, the next highest roll wins")
    print(player1, "are you ready?")
    input("Press enter to roll")
    dice1_bonus=random.randint(1,6)
    dice_output(dice1_bonus)
    player1total=dice1_bonus

    print(player1, "are you ready?")
    input("Press enter to roll")
    dice1_bonus=random.randint(1,6)
    dice_output(dice1_bonus)
    player1total=dice1_bonus
if player1total>player2total:
    print(player1, "is the winner!!!!")
else:
    print(player2, "is the winner!!!!")