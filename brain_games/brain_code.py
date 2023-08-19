import prompt

print('Welcome to the Brain Games!')


def gretting():
  global name
  name = prompt.string('May I have your name? ')
  print('Hello, ' + name + '!')


gretting()
