import random
def get_choices():
    player_choice = input("Enter your choice (rock, paper, scisor): ")
    options = ["rock", "paper", "scisor"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice , 
            "computer" : computer_choice}
    return choices 

def get_winners(player , computer):
    print (f"Player chose {player} and Computer chose {computer}")

    if player == computer :
        print ("Opps!! its a tie")
    elif player == "rock" :
        if computer == "paper" :
            print ("Paper smashes the rock! You lose")
        else :
            print ("Rock destroys the scisor. You win!") 
    elif player == "paper" :
        if computer == "rock" :
            print ("Paper smashes the rock! You win!")
        else :
            print ("Scisor cuuts the paper. You lose!")
        
    elif player == "scissor" :
        if computer == "paper" :
            print ("Scisor cuts the paper! You Win!")
        else :
            print ("Rock destroys the scisor. You lose!")
    
    




choice = get_choices()
winner = get_winners(choice["player"], choice["computer"])


