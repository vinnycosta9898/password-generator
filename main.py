import string
import random

class PasswordGenerator:

    def __init__(self):
        self.ascii_lowercase = string.ascii_lowercase
        self.ascii_uppercase = string.ascii_uppercase
        self.ascii_letters = string.ascii_letters
        self.ascii_digits = string.digits
        self.ascii_symbols = string.punctuation

    def passwordGen(self, nChar, nNumbers, nSymbols):
        self.password = ""
        self.alphabet = list(self.ascii_uppercase + self.ascii_lowercase + self.ascii_letters)
        self.numbers = list(self.ascii_digits)
        self.symbols = list(self.ascii_symbols)
        
        for i in range(0, nChar):
            self.alphabetRandom = random.randint(0, len(self.alphabet) -1)
            self.password += self.alphabet[self.alphabetRandom] 
        
        for j in range(0, nNumbers):
            self.numberRandom = random.randint(0, len(self.numbers) -1)
            self.password += self.numbers[self.numberRandom]
        
        for k in range(0, nSymbols):
            self.symbolsRandom = random.randint(0, len(self.symbols) -1)
            self.password += self.symbols[self.symbolsRandom]
        print(self.password)

passWordGenerator = PasswordGenerator()
print(passWordGenerator.passwordGen(3, 1, 1))