dict_1 = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}
num = int(input("enter num"))
tens_digit = num // 10
ones_digit = num % 10
try:
    if num < 11:
        print(dict_1[num])
    elif 10 < num < 20:
        print(" ten " + dict_1[ones_digit])
    elif num % 10 == 0:
        print(dict_1[tens_digit] + " ten ")
    else:
        print(dict_1[tens_digit] + " ten " + dict_1[ones_digit])
except:
    print("Please enter valid number")
