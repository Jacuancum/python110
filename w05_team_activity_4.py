grade = float(input('What is your grade percent? '))

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

sign = ''
last_digit = grade % 10
if last_digit >= 7:
    sign = '+'
elif last_digit <= 3:
    sign = '-'
else:
    sign = ''

if grade >= 93:
    sign = ''
if letter == 'F':
    sign = ''

print()
print (f'Your letter grade is: {letter}{sign}')
print ()
if grade >= 70:
    print ('Congratulations! You passed!')
else:
    print ('You can do it, try again!')
print ()
