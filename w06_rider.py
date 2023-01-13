print ('Please answer the following question to see if you can get on ride:')

ride = False

first_age = float (input ('What is the age of the first rider? '))
first_height = float (input ('What is the height of the first rider (inches)? '))
one_or_two = str (input ('Is there a second rider (yes/no)? '))
one_or_two = one_or_two.lower()

if one_or_two == 'yes':
    second_age = float (input ('What is the age of the second rider? '))
    second_height = float (input ('What is the height of the second rider (inches)? '))
    
    # Rule 1
    if first_height < 36 or second_height < 36:
        ride = False
    else:
        # Rule 3
        if first_age >= 18 or second_age >=18:
            ride = True
        else:
            ride = False

else:
    # Rule 2
    if first_age >= 18 and first_height >= 62:
        ride = True
    else:
        ride = False

if ride:
    print ('Welcome to the ride. Please be safe and have fun!')
else:
    print ('Sorry, you may not ride.')