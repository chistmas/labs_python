import sys

def printProgressBar (iter, total, pref = '', suf = '', dec = 1,
                      leng = 100, fill = '█', printEnd = "\r"):
    
    percent = ("{0:." + str(dec) + "f}").format(100 * (iter / float(total)))
    filledLength = int(leng * iter // total)
    bar = fill * filledLength + '-' * (leng - filledLength)
    print('\r%s |%s| %s%% %s' % (pref, bar, percent, suf), end = printEnd)
    # Print New Line on Complete
    if iter == total: 
        print()
        
if len(sys.argv) == 1:
    FileName = open("sort.txt", 'r+')
else:
    FileName = open(sys.argv[1], 'r+')
data = FileName.readlines()
l = sum(1 for line in "sort.txt")
printProgressBar(0, l / 2, pref = 'Progress:', suf = 'Complete', 
                 leng = 50)
for i in range(len(data)):
    printProgressBar(i, l / 2, pref = 'Progress:', suf = 'Complete', 
                     leng = 50)
    wor = data[i].split()
    wor = sorted(wor, key = len)
    data[i] = " ".join(wor)
data = sorted(data, key = len)
printProgressBar(l / 2, l, pref = 'Progress:', suf = 'Complete',
                 leng = 50)
for i in range(len(data)):
    printProgressBar(l/2 + i, l, pref = 'Progress:', suf = 'Complete',
                     leng = 50)
    FileName.write(data[i])
    FileName.write("\n")
    #print(data[i])
FileName.close()
