#Реализуйте алгоритм перемешивания списка.
import random
spis=[1,2,19,12,"мир"]


def mix_spis (spis):

    for i in range(len(spis)): #функция пермешивания списка
        index_random=random.randint(0,(len(spis)-1)) # гененрируем случайные числа от 0 до 5
        temp=spis[i] #записываем в перменную temp начальный список 
        spis[i]=spis[index_random] #пишем в начальный список новые перемешанные данные
        spis[index_random]=temp #присваеваем его перменной temp
    return spis
print("Исходный список: ")       
print (spis)
print("Перемешанный список: ")
print (mix_spis (spis))