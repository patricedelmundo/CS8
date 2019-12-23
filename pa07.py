#Maria Patricia Del Mundo mgdelmundo@umail.ucsb.edu

def getSortedContain(s,ifile,ofile):
    x=""
    for i in range(25533):
        x+=ifile.readline()
    listA=x.split()
    listA.sort()
    blankSpaceBaby = True
    for character in listA:        
        if ((s in character) and blankSpaceBaby == True):
            ofile.write(character)
            blankSpaceBaby = False
        elif((s in character) and blankSpaceBaby == False):
            ofile.write("\n"+ character)


def getReverseSortedNotContain(s,ifile,ofile):
    x=""
    for i in range(25533):
        x+=ifile.readline()
    listA=x.split()
    listA.sort()
    listA.reverse()
    blankSpaceBaby= True
    for character in listA:
        if((s not in character) and blankSpaceBaby == True):
            ofile.write(character)
            blankSpaceBaby = False
        elif((s not in character) and blankSpaceBaby == False):
            ofile.write("\n"+character)


def getRhymeSortedCount(n,ifile, ofile):
    x=""
    for i in range(25533):
        x+=ifile.readline()
    listA=x.split()
    listB=[]
    for character in listA:
        listB.append(character[::-1])
    listB.sort()
    listA=[]
    for character in listB:
        listA.append(character[::-1])
    blankSpaceBaby = True
    for character in listA:
        if((len(character)==n) and blankSpaceBaby == True):
            ofile.write(character)
            blankSpaceBaby = False
        elif((len(character)==n) and blankSpaceBaby == False):
            ofile.write("\n"+character)
