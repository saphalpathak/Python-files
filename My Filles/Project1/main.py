import random
def r_generator(argu):
    rdm = random.choice(argu)
    return rdm
def winner():
    count = 10
    ai = 0
    pl = 0
    while count>0: 
        ans = r_generator(conditions)
        
        user = input("Enter your choice: ")
        user = user.lower()
        count = count-1
        if((user != "snake") and (user != "gun") and (user != "water")):
            print("Incorrect input")
            continue
        elif(ans == "water" and user == "gun"):
            pick = f"Your guess:{user}\nComputer guess: {ans}"
            ai+=1
        elif(ans == "gun" and user == "water"):
            pick = f"Your guess:{user}\nComputer guess: {ans}"
            pl+=1
        elif(ans == "snake" and user == "gun"):
            pick = f"Your guess:{user}\nComputer guess: {ans}"
            pl+=1
        elif(ans == "gun" and user == "snake"):
            pick = f"Your guess:{user}\nComputer guess: {ans}"
            ai+=1
        elif(ans == "water" and user == "snake"):
            pick = f"Your guess:{user}\nComputer guess: {ans}"
            pl+=1
        elif(ans == "snake" and user == "water"):
            pick = f"Your guess:{user}\nComputer guess: {ans}"
            ai+=1
        elif(ans == user):
            pick = f"Your guess:{user}\nComputer guess: {ans}"
            print("Tied")
        print("     *****RESULT*****     ")
        print(pick)
        print(f"Your score:{pl}\nComputer score:{ai}")
        if(count>0):
            print(f"{count} chnace left!")
            continue
        else:
            print("*****GAME OVER*****")
        if(ai>pl):
            win_loose = "You loose"
            print(win_loose)
        else:
            win_loose = "You win"
            print(win_loose)
        if(win_loose=="You win"):
             print(f"You win in {10-count} chance")
        play_again = input("Play again?\n If yes enter y otherwise enter any key:")
        if(play_again=="y"):
            winner()
        else:
            break               
conditions = ["snake","water","gun"]
print("           ***************************************")
print("              Welcome to snake water gun game!")
print("           ***************************************\n\n")
winner()



