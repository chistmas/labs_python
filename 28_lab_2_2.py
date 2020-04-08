import random
import string
import sys


def printProgressBar(iter, total, pref='', suf='', dec=1,
                     leng=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(dec) + "f}").format(100 * (iter / float(total)))
    filledLength = int(leng * iter // total)
    bar = fill * filledLength + '-' * (leng - filledLength)
    print('\r%s |%s| %s%% %s' % (pref, bar, percent, suf), end=printEnd)
    # Print New Line on Complete
    if iter == total:
        print()


if __name__ == "__main__":
    d = int(input("1--Enter manually \n2--No\n"))
    slova = []
    bukvy = []
    if d == 1:
        a = input("How many words:\n")
        b = input("How many letters:\n")
        razmer = int(input("Size?:\n"))
        a = (a.replace(",", "")).split()
        b = (b.replace(",", "")).split()
        a = (a.replace("[", "")).split()
        b = (b.replace("[", "")).split()
        a = (a.replace("]", "")).split()
        b = (b.replace("]", "")).split()
        for i in range(2):
            t = int(a[i])
            z = int(b[i])
            slova.append(t)
            bukvy.append(z)
    elif d == 2:
        for i in range(2):
            slova.append(int(sys.argv[1 + i]))
            bukvy.append(int(sys.argv[3 + i]))
            razmer = int(sys.argv[5])
    else:
        print("Your choice was wrong!!!")

    i = 0
    f = open("filee.txt", "w+")
    alphabet = list(string.ascii_letters)
    text = ""
    l = len(list(range(razmer * 1000 * 1000)))
    printProgressBar(0, l, pref='Progress:', suf='Complete',
                     leng=50)
    dlina = razmer * 1000000
    while i < dlina:
        printProgressBar(i, l, pref='Progress:', suf='Complete',
                         leng=50)
        stroka = random.choice(slova)
        for j in list(range(stroka)):
            slovo = random.choice(bukvy)
            i += slovo
            if i + 3 <= dlina:
                for k in list(range(slovo)):
                    text += random.choice(alphabet)
                text += " "
                i += 1
            else:
                for k in bukvy:
                    if k == dlina - i + 2:
                        k = 1
                if k == 1:
                    slovo = k
                    i += k
                    for e in list(range(slovo)):
                        text += random.choice(alphabet)
                else:
                    text += random.choice(alphabet)
                    i += k

        text += "\n"
        i += 2
    f.write(text)
    f.close()
