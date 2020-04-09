import random

while True:
    msg1 = "    Games    "
    msg2 = "-------------"
    msg3 = "1 - Number guesser"
    msg4 = "2 - Tic Tac Toe"
    msg5 = "3 - Word Guesser"
    msg6 = "4 - Exit"
    
    print("\t",msg1,"\n\t",msg2,"\n",msg3,"\n",msg4,"\n",msg5,"\n",msg6)
    
    selection = int(input())
   
    if (selection == 1):
        lowrange = int(input("Enter the lower range of values: "))
        highrange = int(input("Enter the upper range of values: "))
        randnum = random.randint(lowrange,highrange)
        print("Guess a number between {0} and {1}". format(lowrange,highrange))
        guess = int(input())
        
        while guess != randnum:
            print("Guess a number between {0} and {1}". format(lowrange,highrange))
            guess = int(input())
            if (guess < randnum):
                print("More")
            elif (guess > randnum):
                print("Less")
            else:
                print("Corrrect!")
                break
    if (selection == 2):
        blankslate = [[1,2,3],
                      [4,5,6],
                      [7,8,9]]
        for row in blankslate:
            for index in row:
                print(index,end = " ")
            print("")
        spotnum = int(input("Choose a spot for your X"))
        blankslate[spotnum] = "X"
        for row in blankslate:
            for index in row:
                print(index,end = " ")
            print("")
        
            
            
        
