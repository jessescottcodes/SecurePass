import os
import time
import sys
import random
import string

os.system("cls")
print("Welcome to SecurePass!")
print("Created by Jesse Scott")
print("v1.1.0")
print()
print("Please wait 9 seconds...")
time.sleep(9)

running = True
while running:
    os.system("cls")
    letters = string.ascii_lowercase
    numbers = string.digits
    punct = string.punctuation
    result = ''.join(random.choice(letters) + random.choice(punct) + random.choice(str(numbers)) for i in range(15))
    print(result)
    print()
    input("PRESS ENTER/RETURN...")