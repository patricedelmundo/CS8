#Maria Patricia Del Mundo mgdelmundo@umail.ucsb.edu

def makeStarDict(x):
    mf1=open(x,"r")
    starDict={}
    for line in mf1:
        y=line.split()
        starDict[y[0]]=[float(y[1]), float(y[2])]
    return starDict

def starDistance(dist1, dist2, starDict):
    starList=[]
    for item in starDict:
        if float(starDict[item][0])<dist2:
            if float(starDict[item][0])>dist1:
                starList.append(item)
    starList.sort()
    return starList

def starAVM(avm1, avm2, starDict):
    starList=[]
    for item in starDict:
        if float(starDict[item][1])<avm2:
            if float(starDict[item][1])>avm1:
                     starList.append(item)
    starList.sort()                 
    return starList

def starMean(avm1, avm2, starDict):
    total=0
    count=0
    for item in starDict:
        if float(starDict[item][1])<avm2:
            if float(starDict[item][1])>avm1:
                total+=float(starDict[item][0])
                count+=1
    return (total/count)
