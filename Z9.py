#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции вводит пользователь через пробел.

number=int(input("Введите число: "))
pos=(input("Введите позиции через пробел: ").split())
pos=list(map(int,pos))
def list_N(number:int):
    list_numbers=[]
    for element in range (-number,number+1):
        list_numbers.append(element)
    return list_numbers
print(list_N(number))

print(pos)

numbers=list_N(number)
dif=[]
def mult_pos(pos):
    mult=1
    i=0

    for i in range(len(pos)):
        index=pos[i]
                
        mult*=numbers[pos[i]]
        i+=1
        return mult


print (mult_pos(pos))

