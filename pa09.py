#Maria Patricia Del Mundo mgdelmundo@umail.ucsb.edu

import urllib.request
def makeCityList(URL):
    city = []
    temp = []
    pop = []
    bigList = []
    mypage=urllib.request.urlopen(URL)
    maxCity = 0
    maxPop = 0
    for line in mypage:
        line=line.decode("ascii")
        city = line.split(' (pop.')[0].split('  ')[1].strip() + ", "
        pop = line.split('):')[-2].split('(pop.')[-1].strip()
        temp = line.split(':')[-1].strip()
        if len(city) > maxCity:
            maxCity = len(city)
        if len(pop) > maxPop:
            maxPop = len(pop)
        bigList.append(city.ljust(23) + "Temp: " + temp + ", Pop: " + pop.rjust(maxPop))
        bigList.sort() 
    for i in range(len(bigList)):
        print(bigList[i])
