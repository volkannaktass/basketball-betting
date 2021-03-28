import json
# first and seconde at the same team

avgList = []       
def firstPlayerRating(avgList):
    avg1 = sum(firstPlayerList)/len(firstPlayerList)
    return avgList.append(avg1)

def secondPlayerRating(avgList):
    avg2 = sum(secondPlayerList)/len(secondPlayerList)
    return avgList.append(avg2)

def thirdPlayerRating(avgList):
    avg3 = sum(thirdPlayerList)/len(thirdPlayerList)
    return avgList.append(avg3)

def average(avgList):
    avg = sum(avgList)/len(avgList)
    first = avgList[0]
    second = avgList[1]
    third = avgList[2]
    if first > second and first > third:
        bestPlayerAverage = first
        bestPlayerName = "First"
        print("First is the scorer player!!!!") 
    elif second > first and second > third:
        bestPlayerAverage = second
        bestPlayerName = "Second"
        print("Second is the scorer player!!!!")
    elif third > first and third > second:
        bestPlayerAverage = third
        bestPlayerName = "Third"
        print("Third is the scorer player!!!!")

    average = { "playerAverage": avg,
                "scorerPlayerAverage" : bestPlayerAverage,
                "bestPlayerName" : bestPlayerName
               } 

    with open('record.txt', 'a') as file:
     file.write(json.dumps(average))
    
  
    return avg 



    

a = int(input("1.MATCH points for first player"))
b = int(input("2.MATCH points for first player"))
c = int(input("3.MATCH points for first player"))
d = int(input("4.MATCH points for first player"))
e = int(input("5.MATCH points for first player"))
f = int(input("6.MATCH points for first player"))
g = int(input("7.MATCH points for first player"))
h = int(input("8.MATCH points for first player"))
j = int(input("9.MATCH points for first player"))
k = int(input("10.MATCH points for first player"))

firstPlayerList = []
firstPlayerList.extend((a,b,c,d,e,f,g,h,j,k))

l = int(input("1.MATCH points for second player"))
m = int(input("2.MATCH points for second player"))
n = int(input("3.MATCH points for second player"))
o = int(input("4.MATCH points for second player"))
p = int(input("5.MATCH points for second player"))
r = int(input("6.MATCH points for second player"))
s = int(input("7.MATCH points for second player"))
t = int(input("8.MATCH points for second player"))
u = int(input("9.MATCH points for second player"))
v = int(input("10.MATCH points for second player"))
secondPlayerList = []
secondPlayerList.extend((l,m,n,o,p,r,s,t,u,v))


a1 = int(input("1.MATCH points for third player"))
b1 = int(input("2.MATCH points for third player"))
c1 = int(input("3.MATCH points for third player"))
d1 = int(input("4.MATCH points for third player"))
e1 = int(input("5.MATCH points for third player"))
f1 = int(input("6.MATCH points for third player"))
g1 = int(input("7.MATCH points for third player"))
h1 = int(input("8.MATCH points for third player"))
j1 = int(input("9.MATCH points for third player"))
k1 = int(input("10.MATCH points for third player"))
thirdPlayerList = []
thirdPlayerList.extend((a1,b1,c1,d1,e1,f1,g1,h1,j1,k1))



firstPlayerRating(avgList)
secondPlayerRating(avgList)
thirdPlayerRating(avgList)
print(average(avgList))
