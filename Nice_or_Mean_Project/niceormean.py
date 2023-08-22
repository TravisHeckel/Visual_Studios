#Python: 3.11.4
#
# Author: Travis Heckel
#
# Purpose: This is a small game of decision making created using different functions
# allow us to use while loops and different variables to accept input and track scores.
#
#
#
# This imports the module required for sounds
from playsound import playsound




def start(nice=0,mean=0,name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    #meaning, if we do not already have this user's name,
    #then they are a new player and we need ot get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name !="":
                    print("\n Welcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice\nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print ("\nThe stranger walks away smiling...")
            nice = (nice+1)
            stop = False
        if pick == "m":
            print("\nThe stranger glaes at you \nmenacingly and storms off...")
            mean = (mean+1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()


def show_score (nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variable so it can use them
        lose(nice,mean,name)
    else:  #Else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    #Substitute the {} wildcard with our variable values
    print ("\nNice job {}, you win! \n Everyone loves you and you've \nmade lots of friends along the way!".format(name))
    #call again thae function and pass in our variable
    playsound('sound/applause.wav')
    again(nice,mean,name)

def lose(nice,mean,name):
    #Substitute the {} wildcard with our variable values
    print ("\nAHHH too bad, game over! \n \n{}, you live in a dirty beat-up \nvan by the river, wrteched and alone!".format(name))
    #call again thae function and pass in our variable
    playsound('sound/booing2.mp3')
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDO you want to play again? (y/n): \n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'Yes', (N) for 'No':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)


if __name__ == "__main__":
    start()

