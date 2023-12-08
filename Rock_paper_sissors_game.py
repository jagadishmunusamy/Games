import random

while True:
    
    choices = ["rock","paper","scissor"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock or paper or scissor ? : ").lower()

    if player == computer:
        print("computer picks ---> " + computer )
        print("player picks ---> " + player)
        print("Match Tie!")
    elif player == "rock":
        if computer == "paper":
             print("computer picks ---> " + computer )
             print("player picks ---> " + player)
             print("You Loose!")
        if computer == "scissor":
            print("computer picks ---> " + computer )
            print("player picks ---> " + player)
            print("You Win!")
    elif player == "paper":
        if computer == "rock":
            print("computer picks ---> " + computer )
            print("player picks ---> " + player)
            print("You Win!")
        if computer == "scissor":
            print("computer picks ---> " + computer )
            print("player picks ---> " + player)
            print("You Loose!")
    elif player == "scissor":
        if computer == "rock":
            print("computer picks ---> " + computer )
            print("player picks ---> " + player)
            print("You Loose!")
        if computer == "paper":
            print("computer picks ---> " + computer )
            print("player picks ---> " + player)
            print("You Win!")

    play_again = input("play again? (yes/no) : ").lower()
    if play_again != "yes":
        break
print("bye")
        

        
        
        
    
 
    

