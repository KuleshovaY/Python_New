# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()

a_list = list (input('Введите элементы списка: '))
for i in range(0, len(a_list)-1, 2):
    a_list[i], a_list[i+1] = a_list[i+1], a_list[i]


<<<<<<< HEAD
print(a_list)
=======
print(a_list)

>>>>>>> 439ae4114cbdb0a84779c57021e0fdad836dd26f
