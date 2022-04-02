def countWords():
    fileName=input("Enter File Name: ")

    numberOfWords=0

    openFile=open(fileName, 'r')
    for line in openFile:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
    print("Number Of Words: ")
    print(numberOfWords)

countWords()