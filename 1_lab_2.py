import random
import string
a = list(range(4, 7))
b = list(range(6, 10))
size = 200
i = 0
f= open("filee.txt","w+")
alphabet = list(string.ascii_letters)
text = ""

while i < size * 1000 * 1000:
    stroka = random.choice(a)
    for j in list(range(stroka)):
        slovo = random.choice(b)
        i += slovo
        for k in list(range(slovo)):
            text += random.choice(alphabet)
        text += " "
    text += "\n"
f.write(text)
f.close()
