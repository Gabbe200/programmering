import os
os.system('cls')

baldur_online = True


if baldur_online:
    while True:
        try:
            height = float(input("Höjd: "))
            break
        except:
            print("Skriv höjd i nummer")
            continue

    if height >= 1.2 and height <= 1.99:
        print("du får åka")

    else:
        print("du kan inte åka")

else:
    print("baldur stäng")

weight = float(input("vikt?:"))
hight = float(input("längd?:"))

print("BMI:", weight / hight ** 2)

radie = float(input("skriv en rAdIe:"))
print("arian är:", radie ** 2 * 3.14159265359)

import random

print("tärningen landa på:", random.randint(2, 12))

dice = int(input("täningen kast?"))

rolls = 0

 
while rolls < dice:
    die = random.randint(1, 6)
    print(die)
    rolls += 1 

