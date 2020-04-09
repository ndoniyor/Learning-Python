#Activity - Intro to Python
#Create a program that does 4 different math functions
#Doniyor Nimatullo
#Started and finished 3/25/20
while True:
    print("Choose an option")
    print("1) Find the square root")
    print("2) Solve the quadratic equation -> ax2 + bx + c = 0")
    print("3) Find the area of a triangle")
    print("4) Calculate the average of 5 grades")

    choice = int(input())
    if choice == 1:
        sqrtval = int(input("Enter in a value: "))
        sqrtval = sqrtval**(0.5)
        print(sqrtval)
        
    if choice == 2:
        print("A = ")
        a = int(input())
        print("B = ")
        b = int(input())
        print("C = ")
        c = int(input())
        
        d = (b**2)-(4*a*c)
        quadvalone = -b-(d**(0.5))
        quadvalone = quadvalone / (2*a)

        quadvaltwo = -b+(d**(0.5))
        quadvaltwo = quadvalone / (2*a)
        
        print(quadvaltwo, "\n")

    if choice == 3:
        print("Base = ")
        b = int(input())
        print("Height = ")
        h = int(input())

        area = 0.5*(b*h)
        print(area,"\n")

    if choice == 4:
        print("Grade 1 = ")
        grade1 = int(input())

        print("Grade 2 = ")
        grade2 = int(input())

        print("Grade 3 = ")
        grade3 = int(input())

        print("Grade 4 = ")
        grade4 = int(input())

        print("Grade 5 = ")
        grade5 = int(input())

        sumval = grade1+grade2+grade3+grade4+grade5
        average = sumval/5

        print(average,"\n")
