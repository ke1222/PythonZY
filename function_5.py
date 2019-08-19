def printChars(ch1,ch2):
    count = 0
    for i in range(ch1,ch2):
        count += 1
        print(chr(i),end = " ")
        if count % 10 == 0:
            print("\n")

def start():
    ch1 = 65
    ch2 = 91
    printChars(ch1,ch2)
start()