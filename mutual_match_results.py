import json


avgListFirst = []
avgListSecond = []
def mutualMatchResults(avgListFirst,avgListSecond):
    avg_first = sum(avgListFirst)/len(avgListFirst)
    avg_second = sum(avgListSecond)/len(avgListSecond)
    
    average = { "MutualMatchResultsFirst": avg_first,
                "MutualMatchResultsSecond": avg_second
               } 

    with open('record.txt', 'a') as file:
     file.write("\n" + json.dumps(average,indent=2) + "\n")
    txt1 = "First Team: {} and Second Team: {}".format(avg_first,avg_second)
    return txt1


a = int(input("1.MATCH points for  Mutual---FIRST TEAM"))
b = int(input("2.MATCH points for  Mutual---FIRST TEAM"))
c = int(input("3.MATCH points for  Mutual---FIRST TEAM"))
d = int(input("4.MATCH points for  Mutual---FIRST TEAM"))
e = int(input("5.MATCH points for  Mutual---FIRST TEAM"))

f = int(input("1.MATCH points for  Mutual---SECOND TEAM"))
g = int(input("2.MATCH points for  Mutual---SECOND TEAM"))
h = int(input("3.MATCH points for  Mutual---SECOND TEAM"))
j = int(input("4.MATCH points for  Mutual---SECOND TEAM"))
k = int(input("5.MATCH points for  Mutual---SECOND TEAM"))


avgListFirst.extend((a,b,c,d,e))
avgListSecond.extend((f,g,h,j,k))
print(mutualMatchResults(avgListFirst,avgListSecond))
