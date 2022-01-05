from random import *
def arvud_loendis():
    """
    функция спрашивает сколько пользователь хочет сгенерировать значений в списке и в каком диапозоне и выводит результаты на экран:числа в указаном диапазоне и среднее положительных и отрицательных чисел
    """
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    s=[]
    pos=[]
    neg=[]
    nol=[]
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",nol)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)

def vahetus(a:int,b:int):
    """
    меняет местами значения mini и maxi если mini больше maxi
    :param int a:первое чилсо
    :param int b:второе число
    :rtype:int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """
    выдает n случайных чисел от а до b
    :param int n:сколько чисел надо с генерировать
    :param int a:минимальное значение в списке 
    :param int b:максимальное значение в списке
    :rtype:int
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:int,n:int,nol:int):
    """
    проверяет и запоминает количество позитивных,негатиных и нулевых значений из списка "loend"
    :param list loend:список чьи значения проверяются
    :param int p:количество позитивных чисел в списке
    :param int n:количество негативных чисел в списке
    :param int nol:количесвто нулевых значений в списке
    :rtype:int
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)
        

def keskmine(loend):
    """
    Находит среднее значание в указаном списке
    :param list loend:список чьё среднее значение надо найти
    :rtype:var
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el):
    """
    Добавляет значения в список куда применина эта функция
    :param list loend:список куда будет добвален/ы элементы
    :param float el:то что будет добавлено в указаный список
    """
    loend.append(el)
    loend.sort()
