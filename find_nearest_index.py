def find_nearest_index(base, number):
    def my_log(x):  # return logarithm value of a number
        n = 1000000
        return n * ((x ** (1 / n)) - 1)

    try:
        if number <= 0 or base <= 0:
            raise Exception
        result = round(my_log(number) / my_log(base))
        return result
    except:
        print("invalid input! please enter correct input")


base = int(input("please enter base: "))
number = int(input("please enter any number: "))
index = find_nearest_index(base, number)
print("nearest index :", index)