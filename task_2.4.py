field = input("Напишите любимые фрукты: ")
name = []
num = 1
for el in range(field.count(' ') + 1):
    name = field.split()
    if len(str(name)) <= 10:
        print(f" {num} {name [el]}")
        num += 1
    else:
<<<<<<< HEAD
        print(f" {num} {name [el] [0:10]}")
=======
        print(f" {num} {name [el] [0:10]}")






>>>>>>> 439ae4114cbdb0a84779c57021e0fdad836dd26f
