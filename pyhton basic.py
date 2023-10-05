import random

#this is the function that returns the winner of rock paper scisors
def get_choices():
     #lets define a disctionary 
     player_choice = input("Enter your choice rock, paper or scisor : ")
     options = ["rock", "paper", "scisor"] #its a list that list among the options
     computer_choice= random.choice(options)
     choices = {"player": player_choice, "computer": computer_choice } # its a disctionary it puts value of player_choice variable at player and computer_choice variable value in computer

     return choices 

# this is the function that compares and returns who wins among person and computer
def get_winners(player, computer):
    print(f"You choose {player} and Computer chose {computer}")
    if player == computer :
        print( "Oops its a tie")
    elif player == "rock" :
        if computer == "paper" :
            print (" Paper smashes the rock! You lose")
        else :
            print ("Rock brakes the scisor! You win!")
    elif player == "paper":
        if computer == "rock":
            print ("Paper smashes the rock! you win!")
        else :
            print ("Scisor cuts paper. You lose")
    elif player =="scisor":
        if computer == "rock":
            print ("Rock brakes the scisor. You lose")
        else:
            print ("Scisor cuts the paper. You win !")

choices = get_choices()
result = get_winners(choices["player"], choices["computer"])

                    


