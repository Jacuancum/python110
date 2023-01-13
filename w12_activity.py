people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# Requirement
# 01. Iterate through the list and display each string to the screen.

# for item in people:
#     print(item)

# 02. Split the string into a name and age and print them to the screen.

# for item in people:
#     parts = item.split()
#     name = parts[0]
#     age = parts[1]
#     print(name)
# for item in people:
#     parts = item.split()
#     name = parts[0]
#     age = parts[1]
#     print(age)

# 03. Find the age that is the youngest.
youngest_age = 999
youngest_name = ''
for item in people:
    parts = item.split()
    name = parts[0]
    age = int(parts[1])
    if age < youngest_age:
        youngest_age = age
        youngest_name = name
print(f'The youngest age is: {youngest_age} and the name is {youngest_name}')

# 04. Keep track of the name of the person that is the youngest.


