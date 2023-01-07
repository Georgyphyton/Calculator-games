#!/usr/bin/env python3
import random
from random import randint
from brain_games.games.logic import hello, question, end


def calculator():
    name = hello()
    print('What is the result of the expression?')
    a = 0
    while a<3:
        i = randint(1, 100)
        b = randint(1, 100)
        c = random.choice('-+*')
        ask = str(i) + ' ' + c + ' ' + str(b)
        if c=='+':
            cor_answer=i+b
        elif c=='-':
            cor_answer=i-b
        else:
            cor_answer=i*b
        a += question(ask, cor_answer, name) 
        if a ==3:
            end(name)

