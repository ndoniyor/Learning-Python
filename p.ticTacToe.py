##UNFINISHED
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
        
