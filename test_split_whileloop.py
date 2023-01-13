while True:
    try:
        age = int(input('How old are you? '))
    except ValueError:
        print('Please enter a valid option.')
        continue
    else:
        break
print(f'Oh I see, I know you are {age} now. XD')
