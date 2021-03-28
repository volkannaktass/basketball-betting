import json

numberDefeatedLst = []
handicapDefeatedLst = []
numberDefeatedLstSecond = []
handicapDefeatedLstSecond = []

def def10matchHand(numberDefeatedLst,handicapDefeatedLst,numberDefeatedLstSecond,handicapDefeatedLstSecond):
    #first TEam
    number_def_avg_first = sum(numberDefeatedLst)/len(numberDefeatedLst)
    hand_def_avg_first = sum(handicapDefeatedLst)/len(handicapDefeatedLst)
    first_num_def_gen = (number_def_avg_first+hand_def_avg_first)/2

    #Second Team
    number_def_avg_second = sum(numberDefeatedLstSecond)/len(numberDefeatedLstSecond)
    hand_def_avg_second = sum(handicapDefeatedLstSecond)/len(handicapDefeatedLstSecond)
    second_num_def_gen = (number_def_avg_second+hand_def_avg_second)/2

    
    average = { "number_def_avg_first": number_def_avg_first,
                "hand_def_avg_first": hand_def_avg_first,
                "number_def_avg_second": number_def_avg_second,
                "hand_def_avg_second": hand_def_avg_second,
                "first_num_def_gen": first_num_def_gen,
                "second_num_def_gen": second_num_def_gen
               } 

    with open('record.txt', 'a') as file:
     file.write("\n" + json.dumps(average,indent=2) + "\n")
    print(first_num_def_gen) 
    return second_num_def_gen





a = int(input("1.MATCH points for  Last 10 number defeated Match--FIRSTTEAM"))
b = int(input("2.MATCH points for  Last 10 number defeated Match--FIRSTTEAM"))
c = int(input("3.MATCH points for  Last 10 number defeated Match--FIRSTTEAM"))
d = int(input("4.MATCH points for  Last 10 number defeated Match--FIRSTTEAM"))
e = int(input("5.MATCH points for  Last 10 number defeated Match--FIRSTTEAM"))
f = int(input("6.MATCH points for  Last 10 number defeated Match--FIRSTTEAM"))
g = int(input("7.MATCH points for  Last 10 number defeated Match--FIRSTTEAM"))
h = int(input("8.MATCH points for  Last 10 number defeated Match--FIRSTTEAM"))
j = int(input("9.MATCH points for  Last 10 number defeated Match--FIRSTTEAM"))
k = int(input("10.MATCH points for Last 10 number defeated Match--FIRSTTEAM"))

numberDefeatedLst.extend((a,b,c,d,e,f,g,h,j,k))


h1 = int(input("1.MATCH points for  same Handicap defeated--FIRSTTEAM"))
h2 = int(input("2.MATCH points for  same Handicap defeated--FIRSTTEAM"))
h3 = int(input("3.MATCH points for  same Handicap defeated--FIRSTTEAM"))
h4 = int(input("4.MATCH points for  same Handicap defeated--FIRSTTEAM"))
h5 = int(input("5.MATCH points for  same Handicap defeated--FIRSTTEAM"))

handicapDefeatedLst.extend((h1,h2,h3,h4,h5))

####SECOND TEAM


s1 = int(input("1.MATCH points for  Last 10 number defeated Match--SECONDTEAM"))
s2 = int(input("2.MATCH points for  Last 10 number defeated Match--SECONDTEAM"))
s3 = int(input("3.MATCH points for  Last 10 number defeated Match--SECONDTEAM"))
s4 = int(input("4.MATCH points for  Last 10 number defeated Match--SECONDTEAM"))
s5 = int(input("5.MATCH points for  Last 10 number defeated Match--SECONDTEAM"))
s6 = int(input("6.MATCH points for  Last 10 number defeated Match--SECONDTEAM"))
s7 = int(input("7.MATCH points for  Last 10 number defeated Match--SECONDTEAM"))
s8 = int(input("8.MATCH points for  Last 10 number defeated Match--SECONDTEAM"))
s9 = int(input("9.MATCH points for  Last 10 number defeated Match--SECONDTEAM"))
s10 = int(input("10.MATCH points for Last 10 number defeated Match--SECONDTEAM"))

numberDefeatedLstSecond.extend((s1,s2,s3,s4,s5,s6,s7,s8,s9,s10))


sh1 = int(input("1.MATCH points for  same Handicap defeated--SECONDTEAM"))
sh2 = int(input("2.MATCH points for  same Handicap defeated--SECONDTEAM"))
sh3 = int(input("3.MATCH points for  same Handicap defeated--SECONDTEAM"))
sh4 = int(input("4.MATCH points for  same Handicap defeated--SECONDTEAM"))
sh5 = int(input("5.MATCH points for  same Handicap defeated--SECONDTEAM"))

handicapDefeatedLstSecond.extend((sh1,sh2,sh3,sh4,sh5))



print(def10matchHand(numberDefeatedLst,handicapDefeatedLst,numberDefeatedLstSecond,handicapDefeatedLstSecond))
