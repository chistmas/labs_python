import math

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

def big_summa(ar, fi, leng):
    spis = 0
    j = math.floor(st/leng)
    while j + leng <= fi and j % leng == 0:
        spis += devision(ar, leng)[math.floor(j / leng)]
        j += leng
    for k in range(j, fi):
        spis += ar[k]
    return spis

def check(ar, st, fi, leng):
    if st == 0:
        return big_summa(ar, fi, leng)
    else:
        return big_summa(ar, fi, leng) - big_summa(ar, st-1, leng)

def division(ar, st, fi):
    leng = math.ceil(len(ar)**0.5) 
    return check(ar, st, fi, leng)

if __name__ == "__main__":
    while True:
        arr = []   
        z = input("Choose how to input data: \n1 -- from text.txt\n2 "
                  "-- manually\n3 -- exit\n")
        try:
            if int(z) == 1:
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
                print(division(arr, st, fin))
                print("")
            elif int(z) == 2:
                try:
                    n = int(input("Enter number of elements : ")) 
                except ValueError:
                    print("Not an integer")
                for i in range(0, n): 
                    try:
                        ele = int(input()) 
                    except ValueError:
                        ele = int(input("Not an integer, try again"))
                    arr.append(ele)
                try:
                    st = int(input("Enter the first element:"))
                    fin = int(input("Enter the last element:"))
                except ValueError:
                    print("Not an integer")
                print(division(arr, st, fin))
                print("")
            elif int(z) == 3:
                break
        except ValueError:
            print("You've chosen something wrong -_-\n")
        
    
    
   

    
