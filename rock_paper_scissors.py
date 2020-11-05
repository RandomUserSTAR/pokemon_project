from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Which one do you want to choose?\n'Rock': 'Rock'\n'Paper': 'Paper'\n'Scissors': 'Scissors'\n'Stop the game': 'Stop': ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
        else:
            print("You win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!")
        else:
            print("You win!")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!")
        else:
            print("You win!")
    elif player == "Stop":
      print("Thanks for playing!")
      break
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
