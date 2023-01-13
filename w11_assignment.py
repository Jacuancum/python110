with open('life-expectancy.csv') as lifedata:
    for line in lifedata:
        newline = line.strip()
        parts = newline.split(',')
        country = parts[0]
        code = parts[1]
        year = parts[2]
        age = parts[3]
        
        largest_age = 0
        largest_age = float(largest_age)
        for max in age:
            if max > largest_age:
                largest_age = max
        print(largest_age)


        interest_year = input('Enter the year of interest: ')
        print(f'The overall max life expectancy is: {largest_age} from {country} in {year}')
        print(f'The overall min life expectancy is: {age} from {country} in {year}')
        print()
        print(f'For the year {interest_year}: ')
        print(f'The average life expectancy across all countries was {age}')
        print(f'The max life expectancy was in {country} with {age:.2f}')
        print(f'The min life expectancy was in {country} with {age:.2f}')