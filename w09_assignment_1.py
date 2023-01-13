print()
print('Welcome to the Shopping Cart Program!')
print()
items = []
item = ''
prices = []
price = 0
selection = ''
while selection != 5:
    print()
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    selection = int(input('Please enter an action: '))

    if selection == 1:
        item = str(input('What item would you like to add? '))
        items.append(item)
        price = int(input('What is the price of '"'"+item+"'"'? '))
        prices.append(price)
        print("'"+item+"'"' has been added to the cart.')
    elif selection == 2:
        print('The contents of the shopping cart are:')
        for item in items:
            print(item)
    elif selection == 3:
        remove_item = input('What do you want to remove? ')
        items.remove(remove_item)
        print('Item removed.')
    elif selection == 4:
        for price in prices:
            prices += price
            print('The total amount :'+prices)
    elif selection > 5:
        print('Sorry, that is not a valid number.')
    else:
        print

print('Thank you. Goodbye.')

print(items)
print(prices)