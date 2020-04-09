#Doniyor Nimatullo
#Tutorial 2.2 - While and Function
#Learn how to use while loops and functions in python
#4/5/20

num = int(input("Enter in a number: "))

if ((num >= 0) and (num <= 10)):
    while (num != 0):
        num = int(num/2)
        print(num,"\n")
        if (num == 0):
            break
else:
    print("invalid")
          
