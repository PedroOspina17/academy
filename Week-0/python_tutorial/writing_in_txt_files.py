import sys

logFile = open("WrittingNumers.txt","w")
entryFile = open("entyFile.txt","w")
for i in range(10):
    print("{},{},{}".format( i,i*2,i*i), file=entryFile)
    print("this is the result number {}".format(i),file=logFile)
logFile.close()
