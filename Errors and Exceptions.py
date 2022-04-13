# Try and exception statements

def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

    # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)

# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

# as try and except statement gives only one exception . Do comment on other one


print("---------------------------------------------------")


# using else with try-except statements
def AbyB(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)


AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

print("---------------------------------------------------")

# Finally keyword

try:
    k = 5 // 0
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    print('This is always executed')

print("---------------------------------------------------")

# using raise keyword to raise an exception

try:
    amount = 1999
    if amount < 2999:

        # raise the ValueError
        raise ValueError("please add money in your account")
    else:
        print("You are eligible to purchase DSA Self Paced course")

# if false then raise the value error
except ValueError as e:
    print(e)
