import datetime
#from random import shuffle
import random
import csv
from firebase import firebase
firebase = firebase.FirebaseApplication('https://singelstraat13.firebaseio.com',None)

huisgenoten = ["Roland","Thomas","Daan"]
wekelijkseTaken = ["Keuken","Toilet en Douche"]
maandelijkseTaken = ["Vloer gang en keuken"]


csvfile = open('huisrooster2.csv', 'wb')
spamwriter = csv.writer(csvfile, delimiter=',')


    
def getHuisgenootVoorTaak(taak, huisgenoten):
    huisgenoot = huisgenoten[0]
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



today = datetime.date(2015, 4, 6)
toAdd = datetime.timedelta(days=7)

random.seed(1)
for weeknummer in range(0,7):
    amountToShuffle = 2
    
    firstpart = huisgenoten[1:1+amountToShuffle]
    random.shuffle(firstpart)
    huisgenoten[1:1+amountToShuffle]= firstpart
    findHuisgenootPerTaak(wekelijkseTaken, huisgenoten, today)
    if weeknummer%4==3:
        findHuisgenootPerTaak(maandelijkseTaken, huisgenoten, today)
    today = today + toAdd
        

