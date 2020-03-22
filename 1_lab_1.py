import math

#razbienie na summy podmassivov
def devision(ar, leng):
    summa = 0
    vse = []
    for i in range(1, math.ceil(len(ar))):
        summa += ar[i-1]
        if i % leng == 0:
            vse.append(summa)
            summa = 0
    if summa != 0:
        vse.append(summa)
    return vse

#summa s 0-go elementa do poslednego zadannogo
def big_summa(ar, fi, leng):
    spis = 0
    j = math.floor(st/leng)
    while j + leng <= fi and j % leng == 0:
        spis += devision(ar, leng)[math.floor(j / leng)]
        j += leng
    for k in range(j, fi):
        spis += ar[k]
    return spis

#konechnaja funkcija 
def check(ar, st, fi, leng):
    if st == 0:
        return big_summa(ar, fi, leng)
    else:
        return big_summa(ar, fi, leng) - big_summa(ar, st-1, leng)

def division(ar, st, fi):
    leng = math.ceil(len(ar)**0.5) 
    return check(ar, st, fi, leng)

arr = []   
z = int(input("Choose how to input data: \n1 -- from text.txt\n2 -- manually\n"))
if z == 1:
    f = open('text.txt', 'r+')
    ff=f.read()
    ff = ff.replace(",","")
    ff = ff.replace("\n", " ")
    ff = ff.replace("["," ")
    ff = ff.replace("]", " ")
    ff = ff.split()
    st = int(ff[-2])
    fin = int(ff[-1])
    arra = ff[:-2]
    arr = []
    for i in range(len(arra)):
        t = int(arra[i])
        arr.append(t)
    f.close()

elif z == 2:
    n = int(input("Enter number of elements : "))  
    for i in range(0, n): 
        ele = int(input()) 
        arr.append(ele) 
    st = int(input("Enter the first element:"))
    fin = int(input("Enter the last element:"))
else:
    print("You've chosen something wrong -_-")

print(division(arr, st, fin))
    
   

    
