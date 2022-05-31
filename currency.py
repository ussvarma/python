import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

number=int(input("please enter number"))

print("{0:n}".format(number))

