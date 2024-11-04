def main():
    print('hello world')

def menu():
    #menu accepts no arguments
    #it takes input on 3 options from the user
    #choice between set min/max, start new game, and exit
    #set choice to 0
    choice = 0
    #show choices
    print("Please choose an option:")
    print("1. Start New Game")
    print("2. Set min/max number")
    print("3. Exit")
    #user makes a choice
    choice = int(input(":> "))
    #if they put less than 1
    while choice < 1:
        print("Error. Try again.")
    if choice == 1:
        print("Loading.... New Game")
    elif choice ==2:
        print("Loading.... Set Range")
        random()
    elif choice== 3:
        print("Exiting Game")
        pass

def return_name():
    #accepts no arguments
    #gets names from user
    #returns names
    player1=input("What is the name of player 1: ")
    player2= input("What is the name of player 2: ")
    return player1, player2

   

def random():
    #accepts no arguments
    #generates random number
    # returns number
    #within the min/max
    import random as r
    #generate min and max
    MIN=int(input("What would you like your MIN to be: "))
    MAX=int(input("What would you like your MAX to be: "))
    
    #generate random number
    num=r.randint(MIN,MAX)
    #return the number generated
    return num
    pass

def guess(num, player1, player2):
    #guess takes arguments from random and return name, which are num, player 1, player2
    #guess will calculate if you got the guess correct, and if you are too high or low
    #guess will also keep track of how many turns have gone
    #make guess to 0
    GUESS1 = 0
    GUESS2 = 0