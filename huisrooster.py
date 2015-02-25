import datetime
#from random import shuffle
import random
import csv
from firebase import firebase
firebase = firebase.FirebaseApplication('https://roosterstanna.firebaseio.com',None)

huisgenoten = ["Gitte","Jean-Marc","Mats","Marinthe","Wes","Bob","Gerdi", "Roland"]
wekelijkseTaken = ["Keuken","Toilet","Douche","Vuilnis(zie Dar)"]
maandelijkseTaken = ["Glas wegbrengen","Vloer gang","Vloer keuken"]
onmogelijkeCombinaties = {"Marinthe":"Keuken", "Marinthe":"Vuilnis(zie Dar)"}


csvfile = open('huisrooster2.csv', 'wb')
spamwriter = csv.writer(csvfile, delimiter=',')


    
def getHuisgenootVoorTaak(taak, huisgenoten):
    huisgenoot = huisgenoten[0]
    if taak=="Keuken" and huisgenoot == "Marinthe":
        return (huisgenoten[1],1)
    if taak=="Vuilnis(zie Dar)" and huisgenoot == "Marinthe":
        return (huisgenoten[1],1)
    if taak=="Vloer keuken" and huisgenoot == "Marinthe":
        return (huisgenoten[1],1)
    return (huisgenoot,0)

def saveHuisgenoot(date,beforeDate,taak,huisgenoot):
    print str(date) + "," +str(beforeDate) + "," + taak + "," + huisgenoot
    print today.strftime('We are the %d, %b %Y')
    spamwriter.writerow([date, beforeDate, taak,huisgenoot])
    new_user = {'name':huisgenoot,'date':date,'beforeDate':beforeDate,'taak':taak,'huisgenoot':huisgenoot}
    result = firebase.post('/taken',new_user)

def findHuisgenootPerTaak(taken,huisgenoten, date):
    beforeDate = date+datetime.timedelta(days=6)
    for taak in taken:
        (huisgenoot,index) = getHuisgenootVoorTaak(taak,huisgenoten)
        huisgenoten.append(huisgenoten.pop(index))
        saveHuisgenoot(date,beforeDate,taak,huisgenoot)    



today = datetime.date(2015, 3, 2)
toAdd = datetime.timedelta(days=7)

random.seed(1)
for weeknummer in range(0,30):
    amountToShuffle = 3
    
    firstpart = huisgenoten[1:1+amountToShuffle]
    random.shuffle(firstpart)
    huisgenoten[1:1+amountToShuffle]= firstpart
    findHuisgenootPerTaak(wekelijkseTaken, huisgenoten, today)
    if weeknummer%4==3:
        findHuisgenootPerTaak(maandelijkseTaken, huisgenoten, today)
    today = today + toAdd
        

