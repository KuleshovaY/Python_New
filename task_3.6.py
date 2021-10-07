# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def my_func(a):
    word = a.split()
    result = []
    for i in word:
        element = str(i)
        first_letter = element[:1].upper()
        u_word = first_letter + element[1:]
        result.append(u_word)
    return result
print(my_func('homework done'))
