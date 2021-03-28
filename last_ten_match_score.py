import json


avgList = []

def last10matchScore(avgList):
    avg = sum(avgList)/len(avgList)
    average = { "last10matchScore": avg } 

    with open('record.txt', 'a') as file:
     file.write("\n" + json.dumps(average,indent = 2) + "\n")
    return avg


a = int(input("1.MATCH points for  Last 10 Match"))
b = int(input("2.MATCH points for  Last 10 Match"))
c = int(input("3.MATCH points for  Last 10 Match"))
d = int(input("4.MATCH points for  Last 10 Match"))
e = int(input("5.MATCH points for  Last 10 Match"))
f = int(input("6.MATCH points for  Last 10 Match"))
g = int(input("7.MATCH points for  Last 10 Match"))
h = int(input("8.MATCH points for  Last 10 Match"))
j = int(input("9.MATCH points for  Last 10 Match"))
k = int(input("10.MATCH points for Last 10 Match"))

avgList.extend((a,b,c,d,e,f,g,h,j,k))
print(last10matchScore(avgList))
