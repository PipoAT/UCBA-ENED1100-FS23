# Advanced Python Syntax Examples/Shortcuts
# Developed by Andrew T. Pipo for ENED1100 Fall Semester 2023

# For increasing or decreasing by a constant value
# [variable_name] += [constant or variable]
# [variable_name] -= [constant or variable]

num = 0 # initalize a variable to a value

num = num + 1 # increments the num variable by 1

num += 1 # this also increments the num variable by 1, but using shorter, cleaner syntax

print(num)

num = num - 1 # decreases the num variable by 1

num -= 1 # this also decreases the num variable by 1, but using shorter, cleaner syntax

print(num)





# For declaring multiple variables to values in the same line
# [variable_name_one], [variable_name_two] = [value_one], [value_two]
varOne, varTwo = 1, 2
print(varOne)
print(varTwo)