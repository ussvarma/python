# welcome to calculator

while True:
    num_1 = int(input("please enter 1st number: "))
    num_2 = int(input("please enter 2st number: "))
    operator = input("""    Press 1 for addition 
    Press 2 for subtraction 
    Press 3 for multiplication 
    Press 4 for division
    """)
    if operator == "1":
        print(num_1 + num_2)
    elif operator == "2":
        print(num_1 - num_2)
    elif operator == "3":
        print(num_1 * num_2)
    elif operator == "4":
        try:
            print(num_1 / num_2)
        except Exception as e:
            print("invalid input")
            print(e)
    else:
        print("Given wrong input")
    repeat = input("Do you want to explore once more then press y or else n")
    if repeat == "n":
        print("Thank you ")
        break
