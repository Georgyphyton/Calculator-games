#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.games.logic import hello, question, end

def parity():
    name = hello()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    a = 0
    while a < 3:
        i = randint(1, 100)
        ask = str(i)
        if i % 2 == 0:
            cor_answer = 'yes'
        else:
            cor_answer = 'no'
        a += question(ask, cor_answer, name)
        if a ==3:
            end(name)
