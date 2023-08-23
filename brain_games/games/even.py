from random import randint
import brain_games.brain_code


def round():
    i = 0
    while i < 3:
        random_number = randint(0, 100)
        print('Question: ' + str(random_number))
        answer = input('Your answer: ')
        if answer == 'yes' or answer == 'no':
            if random_number % 2 == 0 and answer == 'yes':
                print('Correct!')
            elif random_number % 2 != 0 and answer == 'no':
                print('Correct!')
            else:
                if random_number % 2 == 0:
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
