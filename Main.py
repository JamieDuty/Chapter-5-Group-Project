import random as r
def main():
    #has no arguments
    #calls menu
    #runs programs
    option = menu()
    #get the menu
    #get the players 1 and 2
    #get the random number
    #print(option) -testing what the selected choice was
    if option == 1:
        player1, player2 = return_name()
        num=r.randint(1,1000)
        guess(player1, player2, num)
        main()
    elif option == 2:
        num = random()
        player1, player2 = return_name()
        guess(player1, player2, num)
        main()
        

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
    elif choice== 3:
        print("Exiting Game")
    return choice 


def return_name():
    #accepts no arguments
    #gets names from user
    #returns names
    player1 =input("What is the name of player 1: ")
    player2 =input("What is the name of player 2: ")
    return player1, player2
    
   

def random():
    #accepts no arguments
    #generates random number
    #returns number
    #within the min/max
    #generate min and max
    MIN = int(input("What would you like your MIN to be: "))
    MAX = int(input("What would you like your MAX to be: "))
    #generate random number
    num=r.randint(MIN,MAX)
    #return the number generated
    return num
    


def guess(player1, player2, num):
    #guess takes arguments from random and return name, which are num, player 1, player2
    #guess will calculate if you got the guess correct, and if you are too high or low
    #guess will also keep track of how many turns have gone
    #make guess to 0
    #-used to display the number for testing purposes
    
    #make variables for how many turns it takes
    pg1=0
    pg2=0
        
    
    while True:
       
        guess1 = int(input(f"Enter your guess {player1} "))
        pg1=pg1+1
        if guess1 <= 0:
            print("Error. Reinput.")
            guess1 = int(input(f"Enter your guess {player1} "))
        if guess1 < num:
            print("The number is higher.")
        if guess1 > num:
            print("The number is lower.")
        
        if guess1 == num:
            print("You guessed correct.")
            print(f'Player 1 guessed {pg1} times, player 2 guessed {pg2} times.')
            break
            
        guess2 = int(input(f"Enter your guess {player2} "))
        pg2=pg2+1
        if guess2 <= 0:
            print("Error. Reinput.")
            guess2 = int(input(f"Enter your guess {player2} "))
        if guess2 < num:
            print("The number is higher.")
        if guess2 > num:
            print("The number is lower.")
        
        if guess2 == num:
            print("You guessed correct.")
            print(f'Player 1 guessed {pg1} times, player 2 guessed {pg2} times.')
            break
            
main() 
            
        