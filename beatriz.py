word = 'lion'
hint = ''
counter = 0
print('your hint is:' + '_'*len(word))
while word != hint:
    guess = input('what is your guess?  ')
    hint = []
    while len(word) != len(guess):
        print('the number of characters you typed in is not right. Try again.')
        guess = input('what is your guess? ')
        counter += 1
    else:
        for ind,i in enumerate(word):
            if guess[ind] not in word:
                hint.append('_')
            elif word[ind] == guess[ind]:
                hint.append(guess[ind].upper())
            elif guess[ind] in word:
                hint.append(guess[ind])
        counter += 1
        hint = ''.join(hint)
        print("your hint is:" + ' '.join(hint))
        hint = hint.lower()
else:
    print(f'you tried {counter} times ')
    print("that's it! you guessed it!")




 