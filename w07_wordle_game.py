import random
words = ['isabella','school','daddy','computer','python','movie','morning','afternoon','evening','daisy','work','lunch','breakfast','dinner','water','camping','music','violin','piano','holiday','restaurant','pizza','hamburger','noodle','apple','mango','pineapple','orange','science']
secret = random.choice(words)
print(secret)
print()
print('Welcome to the word guessing game!')
print()
spaces = ['_'] * len(secret)
print(spaces)

def letter_post(guess,secret,spaces):
    index = -2
    while index != -1:
        if guess in secret:
            removed_charater = '*'
            secret = secret[:index]+removed_charater+secret[index+1:]
            spaces[index] = guess
        else:
            index = -1
    return(secret,spaces)

def win_check():
    for i in range(0,len(spaces)):
        if spaces[i]=='_':
            return -1
    return 1

num_turns = len(secret)
for i in range(0,num_turns):
    guess = str(input('What is your guess? ')).lower()

    if guess in secret:
        secret,spaces = letter_post(guess,secret,spaces)
        print(spaces)
    else:
        print('Sorry that the letter is not in the word.')
    
    if win_check() == 1:
        print('Congratulations You Won !')
        break
    print('You have '+str(num_turns - i)+' turns left.')



# guess = -1
# guess_time = 0
# while guess !=secret:
#     guess = str(input('What is your guess? ')).lower()
#     guess_time += 1
#     if guess != secret:
#         print()
#         print('Wrong guess, try again!')



# print()
# print('Bingo! You guessd it!')
# print(f'The correct answer is {secret}.')
# # print(f'You guess {guess_time} times.')