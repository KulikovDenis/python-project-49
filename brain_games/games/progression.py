from random import choice, randint
import brain_games.brain_code


text = ' is wrong answer ;(. Correct answer was '
text_1 = "Let's try again, "


def round():
    i = 0
    while i < 3:
        random_number = list(range(randint(1, 30), 100, randint(1, 5)))[:10]
        random_number_1 = choice(random_number)
        index = random_number.index(random_number_1)
        random_number[index] = '..'
        print('Question: ' + ' '.join(map(str, random_number)))
        answer = input('Your answer: ')
        if str(random_number_1) == answer:
            print('Correct!')
        else:
            print(answer + text + str(random_number_1) + '.')
            print(text_1 + brain_games.brain_code.name + "!")
            break
        i = i + 1
    if i == 3:
        print('Congratulations, ' + brain_games.brain_code.name + '!')
