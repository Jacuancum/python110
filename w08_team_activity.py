# first_name = 'Brigham'
# for i, letter in enumerate(first_name):
#     print(f'The letter {letter} is at {i}')

# word = 'commitment'
# favorite_letter = input('What is your favourite letter? ')
# for letter in word:
#     if letter.lower() == favorite_letter.lower():
#         print(letter.upper(),end='')
#     else:
#         print(letter.lower(),end='')


import random
print('Welcome to a word guessing game!')
word = ['science','computer','window','home']
answer = random.choice(word)
print(answer)
length = ['_'] * len(answer)
print(length)
guess = str(input('What is your guess? '))

for letter in answer:
    if letter.lower() == guess.lower():
        print(letter.upper(), end="")
    else:
        print('_', end="")
print()
guess = -1
guess_time = 0
while guess !=answer:
    guess_time += 1

print()
print('Bingo! You guessd it!')
print(f'The correct answer is {answer}.')
print(f'You guess {guess_time} times.')