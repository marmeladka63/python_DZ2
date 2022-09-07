#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции вводит пользователь через пробел.

number=int(input("Введите число: ")) #вводим число элементов
pos=(input("Введите позиции через пробел: ").split()) # разбиваем сторку по пробелу на список строк
pos=list(map(int,pos)) #преобразовываем все элементы в списке из строк в целые числа
def list_N(number:int): #функция, создам список элементов от -N до N
    list_numbers=[]
    for element in range (-number,number+1):
        list_numbers.append(element)
    return list_numbers
print(list_N(number))

print(pos) 

numbers=list_N(number)
def mult_pos(pos): #функция, находим произведение элементов на указанных позициях
    mult=1
    i=0
    for i in range(len(pos)):
        index=pos[i]
        mult*=numbers[index]
        i+=1
    return mult


print (mult_pos(pos))

