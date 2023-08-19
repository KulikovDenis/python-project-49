import prompt

print('Welcome to the Brain Games!')


def gretting():
  global name
  name = prompt.string('May I have your name? ')
  print('Hello, ' + name + '!')


gretting()

print('Answer "yes" if the number is even, otherwise answer "no".')
