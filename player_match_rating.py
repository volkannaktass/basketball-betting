import json



avgList = []
def averageMatchPlayer(avgList):
    avgMatchPlayer = sum(avgList)/len(avgList)

    average = { "avgMatchPlayer": avgMatchPlayer } 

    with open('record.txt', 'a') as file:
     file.write("\n" + json.dumps(average,indent=2) + "\n")
    return avgMatchPlayer 



a = int(input("1.MATCH points for  player"))
b = int(input("2.MATCH points for  player"))
c = int(input("3.MATCH points for  player"))
d = int(input("4.MATCH points for  player"))
e = int(input("5.MATCH points for  player"))
f = int(input("6.MATCH points for  player"))
g = int(input("7.MATCH points for  player"))
h = int(input("8.MATCH points for  player"))
j = int(input("9.MATCH points for  player"))
k = int(input("10.MATCH points for player"))

avgList.extend((a,b,c,d,e,f,g,h,j,k))
print(averageMatchPlayer(avgList))
