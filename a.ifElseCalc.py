#Activity - if else calculator
#Create a four function calculator using if and if else statements
#Doniyor Nimatullo
#3/31/20
while True:
    msg1 = "Calculator"
    msg2 = "----------"
    msg3 = "1 - Addition"
    msg4 = "2 - Subtraction"
    msg5 = "3 - Multiplication"
    msg6 = "4 - Division"

    print("\t",msg1,"\n\t",msg2,"\n",msg3,"\n",msg4,"\n",msg5,"\n",msg6,)

    selection = int(input())

    if (selection == 1):
        msg7 = "Enter in a number: "
        print(msg7)
        numone = int(input())
        msg7 = "Enter in another number: "
        print(msg7)
        numtwo = int(input())
        sumnum = numone + numtwo
        print('The sum is {0}'. format(sumnum))

    elif (selection == 2):
        msg7 = "Enter in a number: "
        print(msg7)
        numone = int(input())
        msg7 = "Enter in another number: "
        print(msg7)
        numtwo = int(input())
        diffnum = numone - numtwo
        print('The difference is {0}'. format(diffnum))
    elif (selection == 3):
        msg7 = "Enter in a number: "
        print(msg7)
        numone = int(input())
        msg7 = "Enter in another number: "
        print(msg7)
        numtwo = int(input())
        prodnum = numone * numtwo
        print('The product is {0}'. format(prodnum))
    else:
        msg7 = "Enter in a number: "
        print(msg7)
        numone = int(input())
        msg7 = "Enter in another number: "
        print(msg7)
        numtwo = int(input())
        quotnum = numone / numtwo
        print('The quotient is {0}'. format(quotnum))

