n = int(input("please enter the number"))

m = ((n - 2) * 2) + 1

e = 1

# prints first line
print("*" + (m * " ") + "*" + (m * " ") + "*")

# prints middle ones
for i in range(1, n - 1):
    m = m - 2
    print(i * " " + "*" + m * " " + "*" + e * " " + "*" + m * " " + "*")
    e = e + 2

# prints last line
print(" " * (n - 1) + "*" + " " * e + "*")
