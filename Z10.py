#Реализуйте алгоритм перемешивания списка.
import random
spis=[1,2,19,12,"Мир"]


def mix_spis (spis):

    for i in range(len(spis)):
        index_random=random.randint(0,(len(spis)-1))
        temp=spis[i]
        spis[i]=spis[index_random]
        spis[index_random]=temp
        return spis
print("Исходный список: ")       
print (spis)
print("Перемешанный список: ")
print (mix_spis (spis))