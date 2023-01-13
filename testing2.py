import random
words = ['school','python','piano','apple']
secret = random.choice(words)
print(secret)
hint = ''
counter = 0
print('_'*len(secret))
print('If you guess a correct letter, it will appear in small letter.')
print('If the letter you guess on the correct place, it will appear in Capital letter.')
while secret != hint:
    guess = input('What is your guess? ')
    hint = []
    while len(secret) != len(guess):
        guess = input('What is your guess? ')
        counter += 1
    else:
        for ind,i in enumerate(secret):
            if guess[ind] not in secret:
                hint.append('_')
            elif secret[ind] == guess[ind]:
                hint.append(guess[ind].upper())
            elif guess[ind] in secret:
                hint.append(guess[ind])
        counter += 1
        hint = ''.join(hint)
        print(''.join(hint))
        hint = hint.lower()
else:
    print(f'You tried {counter} times.')
    print('Congratulation! You guess it!')