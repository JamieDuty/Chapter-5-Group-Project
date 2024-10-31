def main():
    print('hello world')

def menu():
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
    MIN=int(input("What would you like your MIN to be: "))
    MAX=int(input("What would you like your MAX to be: "))
    
    num=r.randint(MIN,MAX)
    return num

def guess():
    pass