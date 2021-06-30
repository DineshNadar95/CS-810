
from random import choice

def get_computer_choice():
    """ randomly choose and return one of 'rock', 'paper', 'scissors' """
    move = choice(['Rock', 'Paper', 'Scissor'])
    return move
thisdict =	{
  "r": "Rock",
  "p": "Paper",
  "s": "Scissor",
  "q": "q"
}

while(True):
    x=input("Please choose 'R', 'P', 'S' or 'Q' to quit:")
    x=x.lower()
    c=thisdict.get(x,"e")
    l=get_computer_choice()
    if(c==l):
        print("Tie:we both choose "+l)
    elif(c=="Rock"):
        if(l=="Scissor"):
            print("Rock beats Scissor -You win!")
        elif(l=="Paper"):  
            print("Paper beats Rock -You loose!")
    elif(c=="Paper"):
        if(l=="Rock"):
            print("Paper beats Rock -You win!")
        elif(l=="Scissor"):  
            print("Scissor beats Paper -You loose!")     
    elif(c=="Scissor"):
        if(l=="Paper"):
            print("Scissor beats Paper -You win!")
        elif(l=="Rock"):  
            print("Rock beats Scissor -You loose!")     
    elif(c=="q"):
        print("Thanks for playing!")
        break                
    elif(c=="e"):
        print("Invalid Entry, Please enter a valid entry")

    


