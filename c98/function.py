def countWordsFromFile():
    fileName=input("enter the file : ")
    numberofwords=0
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        numberofwords=numberofwords+len(words)
    print("number of words " )
    print(numberofwords)
countWordsFromFile()
