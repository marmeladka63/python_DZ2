# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number=int(input("Введите число: "))

def list_from(number:int):
    list_numbers=[]
    fact=1
    for i in range (1,number+1):
        fact*=i
        list_numbers.append(fact)
    return list_numbers
print(list_from(number))