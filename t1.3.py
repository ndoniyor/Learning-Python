#Tutorial 1.3 - Variable input and output
#Create a 4 function calculator using variable inputs and outputs
#Doniyor Nimatullo
#started and finished 3/24/20

msg1 = "Weclome to the Python Mathematica"
msg2 = "Enter in the first value: "
msg3 = "Enter in the second value: "

print(msg1)
value1 = input(msg2)
value2 = input(msg3)

sumval = int(value1) + int(value2)
diffval = int(value1) - int(value2)
prodval = int(value1) * int(value2)
quotval = int(value1) / int(value2)

print('The sum of {0} and {1} is {2}'. format(value1, value2, sumval))
print('The difference of {0} and {1} is {2}'. format(value1, value2, diffval))
print('The product of {0} and {1} is {2}'. format(value1, value2, prodval))
print('The quotient of {0} and {1} is {2}'. format(value1, value2, quotval))
