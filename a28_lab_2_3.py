import sys

def ProgressBar (iter, total, pref = '', suf = '', dec = 1,
                      leng = 100, fill = '█', printEnd = "\r"):
    
    percent = ("{0:." + str(dec) + "f}").format(100 * (iter / float(total)))
    filledLength = int(leng * iter // total)
    bar = fill * filledLength + '-' * (leng - filledLength)
    print('\r%s |%s| %s%% %s' % (pref, bar, percent, suf), end = printEnd)
    if iter == total: 
        print()

def merge(FileName):
    NewFile = open("sorted.txt", 'w')
        
    data = FileName.readlines()
    l = sum(1 for line in "sort.txt")
    ProgressBar(0, l, pref = 'Progress:', suf = 'Complete', leng = 50)
    for i in range(len(data)):
        wor = data[i].split()
        wor = sorted(wor, key = len)
        data[i] = " ".join(wor)
    data = sorted(data, key = len)
    FileName.close()
    
    for i in range(len(data)):
        ProgressBar(i, len(data) - 1, pref = 'Progress:', suf = 'Complete',
                    leng = 50)
        NewFile.write(data[i])
        NewFile.write("\n")
    NewFile.close()

def main():
        if len(sys.argv) == 1:
            FileName = open("sort.txt", 'r+')
        else:
            FileName = open(sys.argv[1], 'r+')
        merge(FileName)
        
if __name__ == "__main__":
    main()