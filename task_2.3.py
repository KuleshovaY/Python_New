season = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}

month = int(input('Введите любой месяц в виде целого числа от 1 до 12: '))
for key in season.keys():
    if month in season [key]:
        print(key)