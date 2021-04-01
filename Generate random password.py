# Random password generator

import string
import random

PassLen = int(input("Enter the length of the string you want: "))
letter1 = string.ascii_lowercase
letter2 = string.ascii_letters
letter3 = string.punctuation
letter4 = string.digits
letter5 = string.ascii_uppercase

result = "".join(random.choice(letter2) for i in range(3)) + "".join(random.choice(letter3) for i in range(2)) + "".join(random.choice(letter5) for i in range(2)) + "".join(random.choice(letter4) for i in range(2)) + "".join(random.choice(letter1) for i in range(3))

p = "".join(random.sample(result, PassLen ))

print(p)