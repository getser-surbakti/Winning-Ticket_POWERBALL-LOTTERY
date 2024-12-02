import urllib.request
import json

#urllib.request.urlretrieve("https://data.ny.gov/api/views/d6yy-54nr/rows.json?accessType=DOWNLOAD","powerball.json")
file = open("powerball.json")
powerballRecords = json.load(file)
file.close()
#print(powerballRecords)
powerballNumberOccurrence = {}
regularNumberOccurence = {}
for powerballRecord in powerballRecords["data"]:
    powerballNumbers = powerballRecord[9]
    #print(powerballNumbers)
    regularNumbersArr = powerballNumbers.split(" ")
    powerballNumber = regularNumbersArr.pop()
    #print(regularNumbersArr)

    for regularNumber in regularNumbersArr:
        if regularNumber in regularNumberOccurence:
            occurences = regularNumberOccurence[regularNumber]
            occurences += 1
            regularNumberOccurence[regularNumber]= occurences
        else:
            regularNumberOccurence[regularNumber] = 1
    if powerballNumber in powerballNumberOccurrence:
            occurences = powerballNumberOccurrence[powerballNumber]
            occurences += 1
            powerballNumberOccurrence[powerballNumber]= occurences
    else:
            powerballNumberOccurrence[powerballNumber] = 1
#print(regularNumberOcurence)
regularNumberOccurenceSorted = sorted(regularNumberOccurence.items(), key=lambda x:x[1], reverse=True)
#print(regularNumberOccurenceSorted) 
powerballNumberOccurenceSorted = sorted(powerballNumberOccurrence.items(), key=lambda x:x[1], reverse=True)
#print(powerballNumberSorted)

regularNumbersSortedByOccurence = list(map(lambda x:x[0], regularNumberOccurenceSorted))
powerballNumbersSortedByOccurence = list(map(lambda x:x[0],powerballNumberOccurenceSorted))
            

winningTicket = " ".join(regularNumbersSortedByOccurence[:5]+powerballNumbersSortedByOccurence[:1])
print("winningTicket: {}".format(winningTicket))

