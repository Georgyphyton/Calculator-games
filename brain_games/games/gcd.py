#!/usr/bin/env python3
from random import randint
from math import gcd
from brain_games.games.logic import hello, question, end


def game_nod():
    name = hello()
    print('Find the greatest common divisor of given numbers.')
    a = 0
    while a < 3:
        i = randint(1, 100)
        b = randint(1, 100)
        ask = str(i) + ' ' + str(b)
        cor_answer = gcd(i, b)
        a += question(ask, cor_answer, name)
        if a == 3:
            end(name)
