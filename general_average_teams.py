import json


def genAverageTeams(first,second,mutualScoreFirst,mutualScoreSecond,parameter,defeatedFirst,defeatedSecond):
    avgFirst = (first + mutualScoreFirst + defeatedFirst)/3
    avgSecond = (second + mutualScoreSecond + defeatedSecond)/3
    average = { "FirstTeamScore": avgFirst,
                "SecondTeamScore": avgSecond
               } 

    with open('record.txt', 'a') as file:
     file.write("\n" + json.dumps(average,indent=2) + "\n")
    print(avgFirst)
    print(avgSecond)
    return lastScore(avgFirst,avgSecond,parameter)

def lastScore(avgFirst,avgSecond,parameter):
    over_under = ""
    lastScore = avgFirst + avgSecond
    if lastScore > parameter:
        print("Your Score is: {} and OVER".format(lastScore))
        over_under = "OVER"
    elif lastScore < parameter:
        print("Your Score is: {} and UNDER".format(lastScore))
        over_under = "UNDER"

  
    average = { "lastScore": lastScore,
                "over_under" : over_under,
                "parameter": parameter
               } 

    with open('record.txt', 'a') as file:
     file.write("\n" + json.dumps(average,indent=2) + "\n")
    return lastScore



first_team =  float(input("Enter FIRST Team Points"))
second_team = float(input("Enter SECOND Team Points"))
mutualScoreFirst = float(input("Enter Mutual Score for First Team"))
mutualScoreSecond = float(input("Enter Mutual Score for Second Team"))
defeatedFirst = float(input("Enter DEFEATED Score for First Team"))
defeatedSecond = float(input("Enter DEFEATED Score for Second Team"))

parameter = float(input("Enter Parameter"))





genAverageTeams(first_team,second_team,mutualScoreFirst,mutualScoreSecond,parameter,defeatedFirst,defeatedSecond)
