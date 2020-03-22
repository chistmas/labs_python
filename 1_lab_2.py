import random
import string
import sys

if __name__ == "__main__":
    d = int(input("1--Enter manually \n2--No\n"))
    slova = []
    bukvy = []
    if d == 1:
        a = input("How many words:\n")
        b = input("How many letters:\n")
        razmer = int(input("Size?:\n"))
        a = (a.replace(",","")).split()
        b = (b.replace(",","")).split()
        for i in range(2):
            t = int(a[i])
            z = int(b[i])
            slova.append(t)
            bukvy.append(z)
    elif d == 2:
        for i in range(2):
            slova.append(int(sys.argv[1 + i]))
            bukvy.append(int(sys.argv[3+i]))
            razmer = int(sys.argv[5])                
    else:
        print("Your choice was wrong!!!")
    
    i = 0
    f= open("filee.txt","w+")
    alphabet = list(string.ascii_letters)
    text = ""

    while i < razmer * 1000 * 1000:
        stroka = random.choice(slova)
        for j in list(range(stroka)):
            slovo = random.choice(bukvy)
            i += slovo + 1
            for k in list(range(slovo)):
                text += random.choice(alphabet)
            text += " "
        text += "\n"
    f.write(text)
    f.close()




