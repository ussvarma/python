class NumberToWords():
    def __init__(self, n):
        self.n = n
        self.tens_digit = n // 10
        self.ones_digit = n % 10
        self.word = ""
        self.dict_1 = {  # dictionary for mapping number to words
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

    def convert_num_word(self, ):
        try:
            if self.n < 11:
                self.word = self.dict_1[self.num]
            elif 10 < self.n < 20:
                self.word = " ten " + self.dict_1[self.ones_digit]
            elif self.n % 10 == 0:
                self.word = self.dict_1[self.tens_digit] + " ten "
            else:
                self.word = self.dict_1[self.tens_digit] + " ten " + self.dict_1[self.ones_digit]
        except:
            print("Please enter valid number")
        return self.word


number = int(input("Enter a valid number below 100"))
result = NumberToWords(number) # created instance
word = result.convert_num_word()
print(word)
