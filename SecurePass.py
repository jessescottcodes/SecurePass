import os
import time
import sys
import random
import string

os.system("cls")
print("Welcome to SecurePass!")
print("Created by Jesse Scott")
print("v1.0.0")

print("Please wait 6 seconds...")
time.sleep(6)

running = True
while running:
    os.system("cls")
    letters = string.ascii_lowercase
    numbers = string.digits
    result = ''.join(random.choice(letters) + random.choice(str(numbers)) for i in range(15))
    print(result)
    print()
    input("PRESS ENTER/RETURN...")