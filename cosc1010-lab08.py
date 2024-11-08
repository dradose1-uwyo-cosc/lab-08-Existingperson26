# Peter Martinez
# UWYO COSC 1010
# 11/7/2024
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to: Teacher during lab sections did the first part for me. had to ask chatgpt for guidance the rest of the way.
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def isUsable(askNum):
    print("Checking Input")
    if isinstance(askNum, (int, float)):
        return True
    if askNum.isdigit():
        return True
    negative = False
    if askNum.startswith("-"):
        negative = True
        return negative

    if "." in askNum:
        checker = askNum.split(".")
        if checker[0].isdigit() and checker[1].isdigit() and len(checker) == 2:
            return True
        else:
            return False

active = True
while active:
    askNum = input("Please input a number that is either an integer or float. Type 'Exit' to stop").lower()
    if askNum != "exit":
        check1 = isUsable(askNum)
        print(check1)

    elif askNum == "exit":
        active = False
        



print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def slopeForm(varM, varB, lowBound, upBound):
    values = []
    try:
        varM = float(varM)
    except ValueError:
        print("The slope (varM) must be a number.")
        return False
    if not isinstance(lowBound, int) or not isinstance(upBound, int):
        print("The lower/upper boundaries need to be integers!")
        return False
    elif lowBound > upBound:
        print("The lower bound cannot be greater than the upper bound!")
        return False
    for intX in range (lowBound, upBound):
        varY = varM * intX + varB
        values.append(varY)
    return values

active = True
while active:
    varM = input("input a number for the slope. Type 'Exit' to stop.")
    if varM.lower() == "exit":
        active = False
        break
    try:
        varB = float(input("Input a number for the y-intercept: "))
        lowBound = int(input("Input a number for the lower X bound: "))
        upBound = int(input("Input a number for the upper X bound: "))
    except ValueError:
        print("Please enter valid numbers for y-intercept and bounds.")
        continue

    print("Calculating...")
    solutions = slopeForm(varM, varB, lowBound, upBound)
    print(solutions)


# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null


def negativeCheck(varA, varB2, varC):
    root = (varB2)**2 - 4*(varA)*(varC)
    if root < 0:
        return False
    else:
        root = root ** 0.5
        return root


active = True
while active:
    varA = (input("Please enter a value for variable A. Type 'exit' to stop."))
    if varA.lower() == "exit":
        active = False
        break
    else:
        try:
            varA = int(varA)
            varB2 = int(input("Please enter a value for variable B: "))
            varC = int(input("Please enter a value for variable C: "))
        except ValueError:
            print("Please enter valid numbers for variables A, B, and C.")
            continue

    quadForm = negativeCheck(varA, varB2, varC)
    if quadForm == False:
        print("Cannot compute negative numbers!")
    else:
        print(f"Solution 1: {(-varB2 + quadForm)/(2*varA)}")
        print(f"Solution 1: {(-varB2 - quadForm)/(2*varA)}")


