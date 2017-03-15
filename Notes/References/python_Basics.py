# Dominique Charlebois
# Python Basics

# Print Hello World
print "Hello World!"

# Declare Variables
X = 5
A = 10

# X is X + A
X = X + A 

# Print X
print X

# Print Variables (String and Number)
print "X = %d" % X 
print "A = %d" % A

#Swapping
temp = A 
A = X
X = temp 

# Print
print "X = %d" % X 
print "A = %d" % A

# Function
# Made a function and Return it
def add():
    C = 5 + 6
    return C 

# Store it into a Global Variable
D = add()

# Print
print D

# Basic Adding Function (Dynamic)
def add(a, b):
    C = a + b
    return C 

# Store it into a Global Variable and Assign a and b
D = add(11, 45)

# Print
print D

# Basic Multiplier Function
def multiply(a, b):
    C = a * b
    return C 

# Store it into a Global Variable and Assign a and b
D = multiply(11, 45)

# Print
print D

# Shorten Version
def multiply(a, b):
    return a * b

print multiply(5, 6)

# Task
# def OddEven (X)
# print out odd or even 

def OddEven (x):    
    if (x % 2 == 0):
        print "Even"
    else:
        print "Odd"

# Returns print and None (Cuz you have no return statement)
print OddEven(3)

# Returns just the Print 
OddEven(5)

# For Loop
def blastOff():
    # Take the input number and set it to var
    var = input("Enter a number: ")
    print "Number Entered is: %d" %var

    for counter in range(var, 0, -1):
        print counter

blastOff()

# For Loop
def blastOff1():
    # Take the input number and set it to var
    var = input("Enter a number: ")
    print "Number Entered is: %d" %var

    for counter in range(1, var+1, 1):
        print counter
    
    print "Blast Off!"

blastOff1()

#List
# Creating an array called arr
arr = [1,2,3,4,5]

i = 0

while i < 5:
    print arr[i]
    i = i + 1