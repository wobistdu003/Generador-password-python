#! /usr/bin/python3

import random

letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
numbers = "1234567890"
characters = "~!@#$%^&*()_+}{[]\|?><.,:;-="

join = f'{letters}{numbers}{characters}'
length = 20
password = random.sample(join, length)
pasword_end = "".join(password)

print ("___________________________________\n")
print(pasword_end)
print ("___________________________________")
