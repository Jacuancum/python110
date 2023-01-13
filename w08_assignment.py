import random
words = ['water','computer','window','lazy']
answer = random.choice(words)
length = ['_'] * len(answer)
print(answer)
print('Welcome to a word guessing game!')
print('First, you have 5 chances to guess one letter each time.')
print('Then you can enter a final guess at the sixth guess.')
print(length)

chance = 5
while chance > 0:
    guess_letter = str(input('\nWhich letter do you guess? '))
    chance -= 1
    print(f'You still have {chance} chances.')

    for letter in answer:
        if letter.lower() == guess_letter:
            print(letter.upper(),end='')
        else:
            print('_ ',end='')

if chance == 0:
    guess = input('\nYour final guess is : ')
    if guess.lower() == answer.lower():
        print('Bingo! You guessed it! Congratulation!')
    else:
        print('Your guess is wrong. I am sorry for you.')
else:
    print()