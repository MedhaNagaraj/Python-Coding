# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:25:32 2020

@author: medha
"""

from random import randint

num = randint(1,101)
guess = []
#print(num)

while(num):
    if (num < 1 or num > 100):
        print('OUT OF BOUNDS')
    
    guess.append(int(input('Enter Your Guess: ')))
        
    if abs(guess[0] - num) <= 10:
        print('WARM')
    else: 
        print('COLD')
        
    print('Ok lets continue')
    print(guess)

    for i in range(1,100):
        guess.append(int(input('Enter your guess: ')))
        
        if abs(guess[i] == num):
            print('You have guessed it correct in {} guesses'.format(len(guess)))
            break
        elif abs(guess[i] - num) < abs(guess[i-1] - num):
            print('Warmer')
        else:
            print('Colder') 
            
        print(guess)
    break