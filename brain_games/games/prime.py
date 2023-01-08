#!/usr/bin/env python3
from random import randint
from brain_games.games.logic import hello, question, end


def prime():
    name = hello()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    a = 0
    while a < 3:
        i = randint(1, 100)
        b = 2
        cor_answer = 'yes'
        ask = str(i)
        if i < 2:
            cor_answer = 'no'
        while b <= i // 2:
            if i % b == 0:
                cor_answer = 'no'
                break
            b += 1
        a += question(ask, cor_answer, name)
        if a == 3:
            end(name)
