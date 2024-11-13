import os
os.system('cls')

__author__  = "Gabriel Forsberg"
__version__ = "1.0.0"
__email__ = "gabriel.forsberg.ga.ntig.se"
import random


while True:
    print("--G i s s a  N u m r e t 1-100--" , "lycka till")

    number = random.randint(1,100)

    tries = 0

    
    while tries < 7:
            try:
                guess = int(input("skriv ditt första försök:"))
                break
            except:
                 print("skulle du kunna skriva ett nummer tack")
    if guess == 0: 
        print("inte riktigt")
        continue 

         
    


    if guess == 7:
        print("nu har du slut på försök")