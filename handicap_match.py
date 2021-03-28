import json


avgList = []

def handicapAverage(avgList):
    avg = sum(avgList)/len(avgList)
    average = { "handicapAverage": avg } 

    with open('record.txt', 'a') as file:
     file.write("\n" + json.dumps(average,indent=2) + "\n")
    return avg


a = int(input("1.MATCH points for  same Handicap"))
b = int(input("2.MATCH points for  same Handicap"))
c = int(input("3.MATCH points for  same Handicap"))
d = int(input("4.MATCH points for  same Handicap"))
e = int(input("5.MATCH points for  same Handicap"))


avgList.extend((a,b,c,d,e))
print(handicapAverage(avgList))
