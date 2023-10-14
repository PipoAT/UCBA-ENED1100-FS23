# Example Python Conditional
# Developed by Andrew T. Pipo for UC Blue Ash ENED1100 Fall 2023

# user input of a numerical value
x = float(input("Input a value between 1 - 10: "))


# if (conditional):
#    code to execute if the condition is true

if (x < 1):
    print("Out of Bounds")

# elif (conditional):
#   code to execute if this condtion is true, while the above one is false

elif (x > 10):
    print("Out of Bounds")

# else:
#   code to execute if none of the above conditions are true

else:
    print("You input the value of: ", x)


# check multiple conditions in one if statement
# if (first conditional or second condtional)
#   code to execute if either conditional is true

if (x < 1 or x > 10):
    print("Out of Bounds")

# if (first conditonal and second conditional)
#   code to execute if both conditionals are true

if (x >= 1 and x <= 10):
    print("You input the value of: ", x)