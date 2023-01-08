#!/usr/bin/env python3
from random import randint
from brain_games.games.logic import hello, question, end


def progress():
    name = hello()
    print('What number is missing in the progression?')
    a = 0
    while a < 3:
        i = randint(1, 20)
        b = randint(1, 10)
        ask = ''
        d = randint(0, 9)
        for g in range(10):
            if g == d:
                cor_answer = i
                ask += '.. '
                i += b
                continue
            ask += str(i) + ' '
            i += b
        a += question(ask, cor_answer, name)
        if a == 3:
            end(name)
