numbers = [42, 25, 18, 83, 23, 85, 38, 2]

largest_so_far = numbers[0]

for number in numbers:
    if number > largest_so_far:
        # This number is larger than the largest we had seen so far

        # So it is now the largest we've seen
        largest_so_far = number

# Now, after the loop we can display it:
print(f"The largest is: {largest_so_far}")



people_info = [['United State',20],['England',24],['Hong Kong',34],['Taiwan',32]]

largest_age = -1
from_country = ''  # It doesn't matter, it just needs to be declared
for item in people_info:
    country = item[0]
    age = item[1]

    if age > largest_age:
        largest_age = age
        from_country = country

print(f'The oldest person is {largest_age} years old, from {from_country}.')
