print()
print('Please enter the following information:')
print()
first_name=input('First name: ')
last_name=input('Last name: ')
email=input('Email address: ')
phone_number=input('Phone number: ')
job_title=input('Job title: ')
id_number=input('ID Number: ')
hair_color=input('Hair color: ')
eyes_color=input('Eyes color: ')
print()
print('The ID Card is:')
print('----------------------------------------')
print(last_name.upper()+', '+first_name.capitalize())
print(job_title.capitalize())
print('ID: '+id_number)
print()
print(email)
print(phone_number)
print('Hair: '+hair_color.capitalize()+'        '+'Eyes: '+eyes_color.capitalize())
print('----------------------------------------')