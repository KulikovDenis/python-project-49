import brain_games.brain_code
from random import randint
from math import sqrt


def divisors(random_number):
    if random_number <= 1:
        return False
    number_sqrt = int(sqrt(random_number))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if random_number % element == 0:
            return False
    return True


def round():
    i = 0
    while i < 3:
        random_number = randint(0, 100)
        print('Question: ' + str(random_number))
        answer = input('Your answer: ')
        if answer == 'yes' or answer == 'no':
            if divisors(random_number) == True and answer == 'yes':
                print('Correct!')
            elif divisors(random_number) == False and answer == 'no':
                print('Correct!')
            else:
                if divisors(random_number) == True:
                    print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                    print("Let's try again, " + brain_games.brain_code.name + "!")
                else:
                    print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                    print("Let's try again, " + brain_games.brain_code.name + "!")
                break
        else:
            print(answer + " is wrong answer ;(. Correct answer was 'yes' or no'.")
            print("Let's try again, " + brain_games.brain_code.name + "!")
            break
        i = i + 1
    if i == 3:
        print('Congratulations, ' + brain_games.brain_code.name + '!')
