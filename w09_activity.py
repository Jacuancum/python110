# list_of_names = []

# name = ''
# while name != 'end':
#     name = input('What is your name? ')
#     list_of_names.append(name)
# print(list_of_names)

# for name in list_of_names:
#     print(name)



price_list = []
price = 0
while price != str('end'):
    price = input('How much is it? ')
    price_list.append(price)
print(price_list)

for price in price_list:
    print(price)

# for price in price_list:
#     print(price)
price_lists = [50,50,50]
total_price = 0
for price in price_lists:
    total_price += price
print(total_price)