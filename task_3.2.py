# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def data_func(name, surname, year_born, city, email, phone):
    return (name, surname, year_born, city, email, phone)

print(data_func(name= 'Sabrina', surname= 'Simon', year_born= '1989', city= 'New York', email= 'sambrina.s@gmail.com', phone= '+18239-234-34-12'))

