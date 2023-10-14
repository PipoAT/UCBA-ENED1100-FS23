# Example Python Loops
# Developed by Andrew T. Pipo for UC Blue Ash ENED1100 Fall 2023

# User input of an integer numerical value
intInput = int(input("Input any integer: "))

# Using a while loop to count up from the user's number to intInput + 5
# define the stop value
intInputPlusFive = intInput + 5

# while (condition):
#   code that is executed while condition is true

while intInput <= intInputPlusFive:
    print(intInput)
    intInput += 1




# Using a for loop to print out the user input ten times
# User input of an integer numerical value
secondIntInput = int(input("Input any second integer: "))

# for variable in range(startIndex, endIndex):
#   code to execute while in range of the indexes

for i in range(0, 10):
    print(secondIntInput, i)
    i += 1
