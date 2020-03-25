FileName = open("sort.txt", 'r+')
data = FileName.readlines()
for i in range(len(data)):
    wor = data[i].split()
    wor = sorted(wor, key = len)
    data[i] = " ".join(wor)
data = sorted(data, key = len)
for i in range(len(data)):
    FileName.write(data[i])
    FileName.write("\n")
    print(data[i])
FileName.close()