#!/usr/bin/env python3
from random import randint
import prompt


def parity():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    a = 0
    while a < 3:
        i = randint(1, 100)
        print('Question: ' + str(i))
        answer = prompt.string('Your answer: ')
        if (i % 2 == 0 and answer == 'yes') or (i % 2 != 0 and answer == 'no'):
            print('Correct!')
        else:
            if i % 2 == 0:
                cor_answer = 'yes'
            else:
                cor_answer = 'no'
            print("'" + answer + "'" + " is wrong answer ;(.", end=' ')
            print("Correct answer was " + "'" + cor_answer + "'.")
            print("Let's try again, " + name + "!")
            break
        a += 1
    if a == 3:
        print('Congratulations, ' + name + '!')
