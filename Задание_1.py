import pyeasyga

def Main_1(res, obj):
    weight, volume, price = 0, 0, 0
    for (choose, item) in zip(res, obj):
        if choose:
            weight += item[0]
            volume += item[1]
            price += item[2]
    if weight > weight or volume > volume:
        price = 0
    return price
def result():
    obj=array
    GA = pyeasyga.GeneticAlgorithm(obj)       
    GA.population_size = 200                   
    GA.fitness_function = Main_1
    GA.run()
    return GA.best_individual()
weight=0
volume=0
array=[]
def readfile():
    string = open('35.txt', 'r') #Мой вариант
    str1 = [str.strip() for str in string]
    string.close()
    global weight
    weight=int(str1[0].split(' ')[0])
    global volume
    volume=int(str1[0].split(' ')[1])
    str1.remove(str1[0])
    for item in str1:
        global array
        items=item.split(' ')
        array.append((int(items[0]),float(items[1]),int(items[2])))
readfile()
k=1
res=result()
print(k,':')
print(res[0],res[1])
