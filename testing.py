# tall = input('How tall are you? ')
# w = str(float(tall)*2)
# print('You are ' + w)

# x = 2
# y = 3
# z = 4
# w = x + y * z
# print(w)

# x = 5
# if x > 5:
#     print("first")
# else:
#     print("second")

# print()
# x = -5
# if x > 5:
#     print("first")
# else:
#     print("second")

print()
print(type(90))

print()
numbers = [1, 2, 3, 4, 5]
numbers.pop()
numbers.remove(1)
print(numbers)

print()
def print_square_value(numbers):
    for number in numbers:
        if number != 2:
            squared = number * number
            print(squared)

numbers = [1, 2, 3, 4]

print_square_value(numbers)
