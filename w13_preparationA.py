def print_double(value):
    double_value = value * 2
    print(double_value)

print_double(12) # outputs 24
print_double(3) # outputs 6
print_double(42) # outputs 84



def print_message(the_message):
    print(the_message)

# it works just fine to use the same variable name as the function did...
the_message = "Message 1"
print_message(the_message)

# but it also works to use a different variable...
user_message = "Message 2"
print_message(user_message)