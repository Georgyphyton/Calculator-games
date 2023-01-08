#!/usr/bin/env python3
import prompt


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return name


def question(ask, cor_answer, name):
    print('Question: ' + ask)
    answer = prompt.string('Your answer: ')
    if str(answer) == str(cor_answer):
        print('Correct!')
        return 1
    else:
        print("'" + str(answer) + "'" + " is wrong answer ;(.", end=' ')
        print("Correct answer was '" + str(cor_answer) + "'.")
        print("Let's try again, " + name + "!")
        return 5


def end(name):
    print('Congratulations, ' + name + '!')
