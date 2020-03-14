import math
arr = list(range(100))

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
    i = 0
    while i + leng <= fi and i % leng == 0:
        spis += devision(ar, leng)[math.floor(i / leng)]
        i += leng
    for j in range(i, fi):
        spis += ar[j]
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
print(division(arr, 55, 71))
