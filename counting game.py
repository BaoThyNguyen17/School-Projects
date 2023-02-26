player1=input("input player 1") 
player2=input("input player 2") 
i=1
player1turn=True 
print("it is", player1,"'s turn")
while i!=15:
    if i<14:
        print(i,i+1,i+2)
        numbers=int(input("how many numbers would you like to choose? 1-3"))
        if numbers<=3 and numbers>0:
            print("player has chosen:")
            for x in range(numbers):
                print(i+x)
            i+=numbers
        else:
            while numbers>3:
                numbers=int(input("error, choose a number beteen 1-3"))
            i+=numbers
    elif i==14:
        print(i,i+1)
        numbers=int(input("how many numbers would you like to choose? 1-2"))
        if numbers<=2 and numbers>0:
            print("player has chosen:")
            for x in range(numbers):
                print(i+x)
            i+=numbers
        else:
            while numbers>2:
                numbers=int(input("error, choose a number beteen 1-2"))
            i+=numbers
                
    if i==15 or i>15:
        print("number 15 reached")
        break
    if player1turn==True:
        player1turn=False
        player2turn=True
        print("it is", player2,"'s turn")
    elif player2turn==True:
        player1turn=True
        player2turn=False
        print("it is", player1,"'s turn") 
print("game ends") 
if player1turn==True:
    print(player2, "won") 
if player2turn==True:
    print(player1, "won") 
