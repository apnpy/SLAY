import numpy as np
import copy

# Заполнение трехдиагональной матрицы
size = int(input("Введите размерность матрицы: \n"))

diag = []
numbers1 = [[0 for j in range(0, size)]
            for i in range(0, size)]

# Цикл для ввода чисел
for a in range(size):
    numbers1 = int(input(f"Введите цифры для главной диагонали для позиции[{a}][{a}] : "))

    # добавление значений в список
    diag.append(numbers1)

diagAbove = []
print("*********")

for k in range(size - 1):
    numbers2 = int(input(f"Введите цифры для диагонали над основной диагональю для позиции[{k}][{k + 1}]: "))

    # добавление значений в список
    diagAbove.append(numbers2)

diagBelow = []
print("*********")

for z in range(size - 1):
    numbers3 = int(input(f"Введите цифры для диагонали под основной диагональю для позиции[{z + 1}][{z}]: "))

    # добавление значений в список
    diagBelow.append(numbers3)
print("*********")

# Заполнение вектора

print("Заполнение вектора b")
b = [0]*size            # Создается список размерности n
for i in range(size):
    b[i] = float(input("Введите число:"))


def tridiag(size, diag, diagAbove, diagBelow):
    global matrix
    matrix = [[0 for j in range(size)]
              for i in range(size)]
    for k in range(size - 1):
        matrix[k][k] = diag[k]
        matrix[k][k + 1] = diagAbove[k]
        matrix[k + 1][k] = diagBelow[k]

    matrix[size - 1][size - 1] = diag[size - 1]

    # так что значения будут выводиться строка за строкой
    for row in matrix:
        print(row)
    return "Трехдиагональная матрица"

print(tridiag(size, diag, diagAbove, diagBelow))

print('Вектор b:', b)
# Решение методом Крамера

A_det = np.linalg.det(matrix)    # Функция нумпая, вычисляющая определитель
print ("Определитель матрицы: ",A_det)
if A_det!=0: # Дальнейшие вычисления только если определитель не равен нулю

    A_det = [A_det]*(size+1)    #Список определителей
    for k in range(size):
        v = copy.deepcopy(matrix)  #Дубликат матрицы
        for i in range(size):
            v[i][k]=b[i]            # Столбцы поочередно заменяются вектором b
        A_det[k+1]=np.linalg.det(v)  # Вычисляется новый определитель

    x=[0]*size # Список размерности n, для решения методом Крамера
    for k in range(size):
        x[k]=A_det[k+1]/A_det[0] # Поочередно делятся "новые" определители, на главный
    print("Определители:", A_det)

    print("Решение методом Крамера:", x)
    print("Решение встроенной функцией:", np.linalg.solve(matrix,b))
else:
    print("Определитель = 0, решения нет :(")