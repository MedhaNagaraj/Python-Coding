# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 01:24:08 2020

@author: medha
"""

from random import randint

num = randint(1,101)
Flag = True
guess = []
counter = 0
print('The secret number is: ' +num)

while(num):
    if (num < 1 or num > 100):
        print('OUT OF BOUNDS!!!')
    
    guess.append(randint(1,101))
        
    if abs(guess[0] - num) <= 10:
        print('WARM')
        Flag = True
    else: 
        print('COLD')
        Flag = False
    
    counter = guess[0]-num
    print('Ok lets continue')
    print(guess)

    if not Flag:
        for i in range(1,100):
                guess.append(randint(1,101))
                print('Enter your guess: '+ str(guess[-1]))
                
                if abs(guess[i] == num):
                    print('You have guessed it correct in {} guesses'.format(len(guess)))
                    print(guess)
                    print(len(guess))
                    break
                elif abs(guess[i] - num) < abs(guess[i-1] - num):
                    print('Warmer')
                else:
                    print('Colder') 
            
    print(guess)
    print(len(guess))
    break

