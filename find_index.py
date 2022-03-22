def my_log(x): #return logarithm value of a number
    n = 1000000
    return n * ((x ** (1 / n)) - 1)


try:
    base = int(input("please enter base: "))
    num = int(input("please enter any number: "))
    if num <= 0 or base <= 0:
        raise Exception
    result = round(my_log(num) / my_log(base))
    print("nearest index :", result)
except:
    print("invalid input! please enter correct input")
