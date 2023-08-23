from random import randint
import brain_games.brain_code
from math import gcd


def round():
    i = 0
    while i < 3:
        random_number_1 = randint(1, 10)
        random_number_2 = randint(1, 10)
        print(f'Question: {random_number_1} {random_number_2}')
        answer = input('Your answer: ')
        if gcd(int(random_number_1), int(random_number_2)) == int(answer):
            print('Correct!') 
        else:
            print(answer + ' is wrong answer ;(. Correct answer was ' + str(gcd(int(random_number_1), int(random_number_2))) + '.')
            print("Let's try again, " + brain_games.brain_code.name + "!")
            break
        i = i + 1
    if i == 3:
        print('Congratulations, ' + brain_games.brain_code.name + '!')
