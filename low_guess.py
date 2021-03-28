import json



# En skorer oyuncu oldugu maclarda takimlarin sayi ortalamasi == a
# takimin son 10 macta attigi ortalama basket sayisi = c
# d == endusuk tahmin
#takimin ayni handikapli maclarinda ortalama attigi basket sayisi == b
def lowGuess(a,c,b):
    d = (a+c)/2
    average = { "lowGuess": d } 

    with open('record.txt', 'a') as file:
     file.write("\n" + json.dumps(average,indent=2) + "\n")
    print(d)
    return generalAverage(d,b)

def generalAverage(d,b):
    e = (d+b)/2
    average = { "GeneralAverage": e } 

    with open('record.txt', 'a') as file:
     file.write("\n" + json.dumps(average,indent=2) + "\n")
    return e


def general_average(a,c,b):
    avg = (a+b+c)/3
    average = { "GeneralAveragediv3": avg } 

    with open('record.txt', 'a') as file:
     file.write("\n" + json.dumps(average,indent=2) + "\n")
    return avg




player_match_rating =  float(input("Enter Player Match Rating"))
last_ten_match_score = float(input("Last 10 match score"))
handicap_match = float(input("Handicap Score History"))
#lowGuess(player_match_rating,last_ten_match_score,handicap_match)

print(general_average(player_match_rating,last_ten_match_score,handicap_match))
