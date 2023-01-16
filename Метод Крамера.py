import numpy as np
import copy

#Ввод размерности матрицы, заполнение матрицы и вектора
size = int(input('Введите размерность матрицы:\n'))

#Заполнение матрицы
array = []
for i in range(size):
    buff = []             # Доп список с помощью которого будет заполняться матрица
    print("№ строки:", i+1)
    for j in range(size):
        value = float(input('Введите число:'))
        buff.append(value)
    array.append(buff)       # Заполнение матрицы построчно

#Заполнение вектора b
print("Заполнение вектора b")
b = [0]*size            # Создается список размерности n
for i in range(size):
    b[i] = float(input("Введите число:"))
# array =[[-10,-5,0,5,10],[3,2,10,0,-10],[-10,-5,6,7,2],[-7,3,10,5,0],[-17,-8,16,12,2]]
# # b = [24.75,34.5,-10.25,-12.92,-25]
# b=[23.75,35,-11.25,-11.25,-22.5]
# size = 5

#Вывод матрицы
print("Матрица А:")
for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=' ')
    print()
print("Вектор b:", b)

#Обусловленность матрицы
result =  np.linalg.cond(array)
print("Число обусловленности матрицы:",result)

#ищем определитель матрицы
A_det = np.linalg.det(array)    # Функция нумпая, вычисляющая определитель
print ("Определитель матрицы: ",A_det)
if A_det!=0: # Дальнейшие вычисления только если определитель не равен нулю

    A_det = [A_det]*(size+1)    #Список определителей
    for k in range(size):
        v = copy.deepcopy(array)  #Дубликат матрицы
        for i in range(size):
            v[i][k]=b[i]            # Столбцы поочередно заменяются вектором b
        A_det[k+1]=np.linalg.det(v)  # Вычисляется новый определитель

    x=[0]*size # Список размерности n, для решения методом Крамера
    for k in range(size):
        x[k]=A_det[k+1]/A_det[0] # Поочередно делятся "новые" определители, на главный
    x_okrug = []
    for i in range(x):
        x_okrug.append(round(x[i], 4))

    print("Определители:", A_det)

    print("Решение методом Крамера:", )
    print("Решение встроенной функцией:", np.linalg.solve(array,b))
else:
    print("Определитель = 0, решения нет :(")
