import random
#Читать данные из файла 35.txt (мой вариант)
w0=0
v0=0
ar0=[]
def DatafromFile():
    string = open('35.txt', 'r')
    str1= [str.strip() for str in string]
    string.close()
    global w0
    w0=int(str1[0].split(' ')[0])
    global v0
    v0=int(str1[0].split(' ')[1])
    str1.remove(str1[0])
    for item in str1:
        global ar0
        items=item.split(' ')
        ar0.append((int(items[0]),float(items[1]),int(items[2])))
DatafromFile()
#1.2 -  жадный выбор, начиная со случайного груза         
pp=[]
newpp=[]
N=200
array=[]
def fun_1():
    ar=sorted(ar0,key=lambda x: x[2])
    global array
    array=ar[::-1]
    for i in range (0,N):
        random.seed()
        individual=random.randint( 0, len(array))
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
        for k in range(0,len(pp[i][0])):
            if pp[i][0][k]==0:
                if w1+array[k][0]<w0 and v1+array[k][1]<v0:
                    pp[i][0][k]=1
                    w1 += array[k][0]
                    v1 += array[k][1]
            else:
                break
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
        r = random.randint(0, round(S))
        s=0
        while s<r and i<len(m_p):
            s+=m_p[i][1][0]
            i+=1
        S-=m_p[i-1][1][0]
        mama=m_p[i-1][0]
        papa = m_p[i-1][0]
        m_p.remove(m_p[i - 1])
        fun_3(mama, papa)
#3.2 -  однородный (каждый бит от случайно выбранного родителя)
def getX(child):
    x=0
    volume = 0
    weight = 0
    for j in range(0, len(child)):
        if child[j] == 1:
            x += array[j][2]
            weight += array[j][0]
            volume += array[j][1]
            if weight>w0 or volume>v0:
                x = 0
                break
    return x
def fun_3(mama, papa):
    chil=[]
    for i in range(0,len(mama)):
        random.seed()
        individual = random.random()
        if (individual<0.5):
            chil.append(mama[i])
        else:
            chil.append(papa[i])
    baby=[]
    baby.append(chil)
    baby.append([getX(chil)])
    newpp.append(baby)
#4.2 - случайное изменение 3х битов у 5% особей
def fun_4():
    chil = []
    for i in range(0, int(len(chil) * 0.05)):
        individual = random.randint(0, len(chil) - 1)
        rdn = random.randint(0, 29)
        chil[individual][rdn] = chil[individual][rdn] ^ 1
#5 - Формирование новой популяции
def fun_5():
    global pp
    r_pp=sorted(pp+newpp,key=lambda x: x[1])
    r_pp=r_pp[::-1]
    pp=r_pp[0:200]   
#6. Запуск работы алгоритма (до 100 поколений)
def fun_6(gen):
    global array
    array = []
    fun_1()
    for k in range(0,gen):
        fun_2()
        fun_4()
        fun_5()
    return pp[0]
res = fun_6(100)
print(res[1],res[0])

