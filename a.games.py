##Activity - Games
##Create a program that allows the user to select between 3 games: number guesser, dice roll, and word guesser.
##Doniyor Nimatullo
##4/9/20

import random

while True:
    msg1 = "    Games    "
    msg2 = "-------------"
    msg3 = "1 - Number guesser"
    msg4 = "2 - Dice Roll"
    msg5 = "3 - Word Guesser"
    msg6 = "4 - Exit"

    print("\t",msg1,"\n\t",msg2,"\n",msg3,"\n",msg4,"\n",msg5,"\n",msg6)

    selection = int(input())

    if (selection == 1):
        lowrange = int(input("Enter the lower range of values: ")) #user inputs a range of values for the random # generator
        highrange = int(input("Enter the upper range of values: "))
        randnum = random.randint(lowrange,highrange) #generates random number between specified range
        guess = 0
        
        while guess != randnum:
            print("Guess a number between {0} and {1}". format(lowrange,highrange))
            guess = int(input())
            if (guess < randnum):  #if the user input is less than the generated number, the program specifies that the actual number is greater
                print("More")
            elif (guess > randnum):#if the user input is greater than the generated number, the program specifies that the actual number is less
                print("Less")
            else:
                print("Corrrect!")
                break
    if (selection == 2):
        choice = input("Are you ready to roll the dice? (Y/N)")
        if choice == "Y" or choice == "y":
            dice1 = random.randint(1,6) #two random number generators between 1 and 6 to simulate dice.
            dice2 = random.randint(1,6)
            dicesum = dice1 + dice2 #finds sum of dice values
            print("Dice 1 rolled a {0}, dice 2 rolled a {1}, the sum of these values is {2}". format(dice1,dice2,dicesum))

    if(selection == 3):
        word = "orange"
        a = ["_","_","_","_","_","_"] #list of blanks
        print(*a) #prints the formatted value of the list without the "" and []
        turns = 10
        while turns != 0: #turns counts down from 10
            print("Guess the word or the letters")
            guess = input()
            if guess == "o":
                print ("Correct, guess another")
                a[0] = "o" #replaces list value with guessed letter
                print(*a)
                turns -= 1 #subtracts turn
                print("Turns left: {0}". format(turns))
   
            elif guess == "r":
                print ("Correct, guess another")
                a[1] = "r"
                print(*a)
                turns -= 1
                print("Turns left: {0}". format(turns))

            elif guess == "a":
                print ("Correct, guess another")
                a[2] = "a"
                print(*a)
                turns -= 1
                print("Turns left: {0}". format(turns))
                
            elif guess == "n":
                print ("Correct, guess another")
                a[3] = "n"
                print(*a)
                turns -= 1
                print("Turns left: {0}". format(turns))

            elif guess == "g":
                print ("Correct, guess another")
                a[4] = "g"
                print(*a)
                turns -= 1
                print("Turns left: {0}". format(turns))

            elif guess == "e":
                print ("Correct, guess another")
                a[5] = "e"
                print(*a)
                turns -= 1
                print("Turns left: {0}". format(turns))
                
            elif guess == word:
                print("Correct!")
                break
            else:
                print("Incorrect")
                turns -= 1
