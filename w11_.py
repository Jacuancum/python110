with open('life-expectancy.csv') as lifedata:
    for line in lifedata:
        newline = line.strip()
        parts = newline.split(',')
        country = parts[0]
        # code = parts[1]
        # year = parts[2]
        # age = float(parts[3])
        # max_life = age[0]
        # for max in age:
        #     if max > max_life:
        #         max_life = max
        # print(max_life)
        print(f'Country: {country}, ')