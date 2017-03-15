# Dominique Charlebois
# Python - Recursion

# Recursive definition -> n! = n(n-1)!
def factorial(n):
    # Print statement
    print "N is", n
    # If statement
    if n == 0:
        # base case
        return 1
    else:
        #recursive case
        result =  n * factorial(n-1)
        print "N-1 is", n-1
        return result
# Call function
print factorial(4)

# Recursive def -> 2 * 2^(n-1)
def power2(n):
    # base case n=0, 2^0 = 1
    if n == 0:
        return 1
    else:
        return 2 * power2(n-1)
# Call function
print power2(2)

# Fibonacci Numbers:
# f(0) = 0
# f(1) = 1
# Sequence: 0,1,1,2,3,5,8, ...
# Recursive definition -> f(n) = f(n-1)+f(n-2)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print fib(8)

# Efficient -> Not Recursive
def fibIt(n):
    f0 = 0
    f1 = 1
    for i in range(n):
        f0, f1 = f1, f0 + f1
        # f0 = f1
        # f1 = f0 + f1
    return f0

print fibIt(8)
