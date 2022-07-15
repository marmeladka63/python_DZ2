# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
import math

number=input("Введите вещественное число: ")
#number=math.fabs(numbers)

def sum_nambers(number):
    
    str_number=str(number)
    str_number=str_number.replace(',','')
    lst_str=list(str_number)
    lst_num=map(int,lst_str)
    s=sum(lst_num)
    return s
    
    
print(sum_nambers(number))
# если ввести число с минусом -код не работает. Нашла модуль abc, но на него ругается, если подставить

