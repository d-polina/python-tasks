# Задание: в текстовом файле находится цепочка из символов латинского алфавита A, B, C. Найти длину самой длинной подцепочки, состоящей из символов B.

# Два способа решения: 1) разбиение строки, 2) перебор символов и подсчет цепочек по ходу перебора

# 1 способ: 
#  - замена ненужных символов на пробелы
#  - разбиение строки по пробелам
#  - поиск кусочков наибольшей длины


s =  open('24.txt').readline() # открываем строчку
print(s) # печатаем строчку, чтобы проверить работает ли

s =  open('24.txt').readline()
s = s.replace('A',' ').replace('C',' ') # все буквы А и С заменяются на пробел 
print(s)

s = open('24.txt').readline()
s = s.replace('A',' ').replace('C',' ')
print(s.split()) # split - разбиение строки на части, по умолчанию разбивание происходит по пробелам

s = open('24.txt').readline()
s = s.replace('A',' ').replace('C',' ')
print(max(s.split())) # чтобы найти строчку из символов одной буквы, можно использовать max, но подвох в том, что аргумент у max - split (строка), а строки на максимальность проверяются по своему (питон проверяет строки в алфавитном порядке)

s = open('24.txt').readline()
s = s.replace('A',' ').replace('C',' ')
print(max(s.split(),key=len)) # ,key - специальный параметр, который специально говорит, что мы хотим найти максимальную строчку и выведется сама строка

s = open('24.txt').readline()
s = s.replace('A',' ').replace('C',' ')
print(len(max(s.split(),key=len))) # len вначале выведет просто цифру

#иной вариант подсчета строки:
print(max(len(c) for c in s.split()))


# 2 способ - Перебор символов
#  - создадим счетчик

s = open('24.txt').readline()
с = m = 0 # создаем два счетчика со значением 0
for i in range(len(s)): # перебираем все символы s[i]:
    if s[i] == 'B': # если s[i] равно B, то
        с += 1 # счетчик с - счетчик текущий, который считает кол-во идущих подряд буковок B на данный момент и как только мы находит букву B, то счетчик с увеличивается на единицу
        m = max(m,с) # в тот же момент мы проверяем счетчик с со счетчиком m, который хранит в себе максимальное значение с за все время перебора
    else: 
        с = 0 # иначе если мы встретим не букву B, то счетчик с сбрасывается до 0
print(m) # печатаем максимальную длину строки B