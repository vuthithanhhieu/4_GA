import random
import copy
#Читать данные из файла 35.txt (мой вариант)
w0=0
v0=0
ar0=[]
def DatafromFile():
    string = open('35.txt', 'r')#Мой вариант
    str1= [str.strip() for str in string]
    string.close()
    global w0
    w0=int(str1[0].split(' ')[0])#Вес
    global v0
    v0=int(str1[0].split(' ')[1])#Объем
    str1.remove(str1[0])
    for item in str1:
        global ar0
        items=item.split(' ')
        ar0.append((int(items[0]),float(items[1]),int(items[2])))
DatafromFile()#запуститьт функции
#1.2 -  жадный выбор, начиная со случайного груза         
pp=[] #Популяция
newpp=[]#новая популяция
N=200 #Количество особей
array=[]
def fun_1():
    ar=sorted(ar0,key=lambda x: x[2])#Сортировка массива
    global array
    array=ar[::-1]
    for i in range (0,N):
        random.seed()
        individual=random.randint( 0, len(array)) #выборка случайного 
        w1=0
        v1=0
        pp.append([])
        pp[i].append([])
        for j in range(0,individual):
            pp[i][0].append(0) 
        for j in range(individual,len(array)):
            if w1+array[j][0]<w0 and v1+array[j][1]<v0: 
                pp[i][0].append(1) 
                w1+=array[j][0]
                v1+=array[j][1]
            else:
                pp[i][0].append(0)
        for k in range(0,len(pp[i][0])):#если выборка случайного в конце->добавляем из начала.
            if pp[i][0][k]==0:
                if w1+array[k][0]<w0 and v1+array[k][1]<v0:
                    pp[i][0][k]=1
                    w1 += array[k][0]
                    v1 += array[k][1]
            else:
                break
def getY():#приспособленность
    for i in range(0,len(pp)): 
        x = 0
        volume=0
        weight=0
        for j in range(0,len(pp[i][0])):
            if pp[i][0][j]==1:
                x+=array[j][2]
                weight+=array[j][0]
                volume+=array[j][1]
                if weight>w0 or volume>v0:
                    x=0
                    break
            pp[i].append([x])
#2.1 - выбор каждой особи пропорционально приспособленности (рулетка)
def fun_2():
    S=0
    m_p=pp.copy()
    for k in range(0,len(pp)):
        S+=pp[k][1][0]
    while len(m_p)>0:
        i = 0
        random.seed()
        r = random.randint(0, round(S))#запускаем "рудетку" 
        s=0
        while s<r and i<len(m_p): #Выбрать маму
            s+=m_p[i][1][0]
            i+=1
        S-=m_p[i-1][1][0]
        m=m_p[i-1][0]
        m_p.remove(m_p[i - 1])
        i = 0
        random.seed()
        r = random.randint(0, round(S))#запускаем "рудетку" 
        s=0
        while s<r and i<len(m_p):#Выбрать папу
            s+=m_p[i][1][0]
            i+=1
        S-=m_p[i-1][1][0]
        p = m_p[i-1][0]
        m_p.remove(m_p[i - 1])
        fun_3(m, p)
        
#3.2 -  однородный (каждый бит от случайно выбранного родителя)
def getX(c):#приспособленность (число )
    x=0
    volume = 0
    weight = 0
    for j in range(0, len(c)):
        if c[j] == 1:
            x += array[j][2]
            weight += array[j][0]
            volume += array[j][1]
            if weight>w0 or volume>v0:
                x = 0
                break
    return x
def fun_3(m, p):# выбрать из мамы и папы 
    c=[]
    for i in range(0,len(m)):
        random.seed()
        individual = random.random()#случайный родитель 
        if (individual<0.5):
            c.append(m[i])
        else:
            c.append(p[i]) 
    b=[] #полученный массив детей 
    b.append(c) 
    b.append([getX(c)])
    newpp.append(b)#Добавить в новой популяции.
#4.2 - случайное изменение 3х битов у 5% особей
def fun_4():
    c = []
    for i in range(0, int(len(c) * 0.05)):#5% особей
        individual = random.randint(0, len(c) - 1)
        rdn = random.randint(0, len(array))#генерируем случайное 
        c[individual][rdn] = c[individual][rdn] ^ 1
#5 - Формирование новой популяции
def fun_5():
    global pp
    for i in range(0,len(pp)):
        pp[i][1][0]=pp[i][1][0]*0.8
    r_pp=sorted(pp+newpp,key=lambda x: x[1])#Сортировка
    r_pp=r_pp[::-1]
    pp=r_pp[0:200]   
#6. Запуск работы алгоритма (до 100 поколений)
def fun_6(gen):
    global pp
    pp = []
    global newpp
    newpp = []
    global array
    array = []
    fun_1()
    getY()
    for k in range(0,gen):
        fun_2()
        fun_4()
        fun_5()
    return pp[0]
res = fun_6(100)
print(res[1],res[0])

