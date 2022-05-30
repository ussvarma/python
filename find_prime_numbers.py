def find_prime(num):
    """

    :param num:
    :return: prime numbers below given number
    """
    for i in range(2, num):
        count = 0
        for j in range(2, i + 1):
            if i % j == 0:
                count += 1
        if count <= 1:
            print(i)


num = int(input("Please enter number above 1 "))
find_prime(num)
