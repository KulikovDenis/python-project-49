import brain_games.brain_code
from random import randint
from math import sqrt


text = ' is wrong answer ;(. Correct answer was '
text_1 = "Let's try again, "


def divisors(random_number):
    if random_number <= 1:
        return False
    number_sqrt = int(sqrt(random_number))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if random_number % element == 0:
            return False
    return True


def round():  # noqa: C901
    i = 0
    while i < 3:
        random_number = randint(0, 100)
        print('Question: ' + str(random_number))
        answer = input('Your answer: ')
        if answer == 'yes' or answer == 'no':
            if divisors(random_number) is True and answer == 'yes':
                print('Correct!')
            elif divisors(random_number) is False and answer == 'no':
                print('Correct!')
            else:
                if divisors(random_number) is True:
                    print("'no'" + text + "'yes'" + ".")
                    print(text_1 + brain_games.brain_code.name + "!")
                else:
                    print("'yes'" + text + "'no'" + ".")
                    print(text_1 + brain_games.brain_code.name + "!")
                break
        else:
            print(answer + text + "'yes' or no'.")
            print(text_1 + brain_games.brain_code.name + "!")
            break
        i = i + 1
    if i == 3:
        print('Congratulations, ' + brain_games.brain_code.name + '!')
