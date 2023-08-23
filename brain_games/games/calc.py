from random import randint, choice
import brain_games.brain_code


text = ' is wrong answer ;(. Correct answer was '
text_1 = "Let's try again, "


def round():  # noqa: C901
    i = 0
    while i < 3:
        random_number_1 = randint(0, 10)
        random_number_2 = randint(0, 10)
        operations = choice(['+', '-', '*'])
        print(f'Question: {random_number_1} {operations} {random_number_2}')
        answer = input('Your answer: ')
        if operations == '+':
            result = int(random_number_1 + random_number_2)
            if result == int(answer):
                print('Correct!')
            else:
                print(answer + text + str(result) + '.')
                print(text_1 + brain_games.brain_code.name + "!")
                break
        elif operations == '-':
            result = int(random_number_1 - random_number_2)
            if result == int(answer):
                print('Correct!')
            else:
                print(answer + text + str(result) + '.')
                print(text_1 + brain_games.brain_code.name + "!")
                break
        elif operations == '*':
            result = int(random_number_1 * random_number_2)
            if result == int(answer):
                print('Correct!')
            else:
                print(answer + text + str(result) + '.')
                print(text_1 + brain_games.brain_code.name + "!")
                break
        i = i + 1
    if i == 3:
        print('Congratulations, ' + brain_games.brain_code.name + '!')
