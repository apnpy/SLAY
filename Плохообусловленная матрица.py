import numpy as np
import copy
import math
from prettytable import PrettyTable
import matplotlib.pyplot as plt

# Плохо обсловленная матрица
# bad_array = [[1, 0.5, 0.333, 0.25], [0.5, 0.333, 0.25, 0.2], [0.333, 0.25, 0.2, 0.166], [0.25, 0.2, 0.166, 0.14]]
# bad_c = [1.0001, 4, 8, 3]
bad_array=[[1,3,2,4], [1.0001,3,2,4], [5,2,8,7], [3,6,2,9]]
bad_c = [36,36.001,79,67]
size = 4

#Обусловленность матрицы
result =  np.linalg.cond(bad_array)
print("Число обусловленности матрицы:",result)

# Решение без погрешностей

def no_error():
    global D_det
    D_det = np.linalg.det(bad_array)        #Поиск определителя плохообусловленной матрицы
    D_det = [D_det] * (size+1)      # Список определителей
    
    for s in range(size):
        v = copy.deepcopy(bad_array) #Дубликат матрицы
        for i in range(size):
            v[i][s] = bad_c[i]         # Столбцы поочередно заменяются вектором c
        D_det[s + 1] = np.linalg.det(v) # Вычисляется новый определитель

    global x
    x = [0] * size # Список размерности n, для решения методом Крамера
    for s in range(size):
        x[s] = D_det[s + 1] / D_det[0] # Поочередно делятся "новые" определители, на главный
    print("Решение методом Крамера:", x)
    print("Решение встроенной функцией:", np.linalg.solve(bad_array, bad_c))
    
    return x

def eps_norm(m):
    global error_list
    error_list = []
    global norm
    norm = [0] * m
    
    for k in range(m):
        c_copy = copy.deepcopy(bad_c) #Дубликат матрицы для дальнейших вычислений
        eps = float(input('Введите погрешность: '))
        error_list.append(eps) # Заполнение списка введенными погрешностями
        for i in range(size):
            c_copy[i]=c_copy[i] + eps   #Прибавление погрешностей к значениям вектора c


        for s in range(size):
            v = copy.deepcopy(bad_array)
            for i in range(size):
                v[i][s] = c_copy[i]  # Столбцы поочередно заменяются "испорченным" вектором c
            D_det[s+1] = np.linalg.det(v) # Вычисляется новый определитель

        x_eps = [0]*size
        for s in range(size):
            x_eps[s] = D_det[s+1]/D_det[0] # Поочередно делятся "новые" определители, на главный
            norm [k] += (x[s]-x_eps[s])**2 # Вычисление нормы оригинальной матрицы и с погрешностью
        norm[k] = math.sqrt(norm[k])
    return norm, error_list

def table_(error_array, norm):
    table = PrettyTable(error_array) # Построение таблицы
    table.add_row(norm[:])
    print(table)

def plot_(norm, error_list):
    plt.plot(error_list,norm)
    plt.xlim([-2,2])
    plt.ylim([4,20])
    plt.grid()
    plt.show()

print('\nРабота с плохо обусловленной матрицей:\n', bad_array)
print ('Вектор c:', bad_c)


print(no_error())
m = int(input('Введите количество погрешностей:'))
print(eps_norm(m))
print(table_(error_list, norm))
print(plot_(norm, error_list))




