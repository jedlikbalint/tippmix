from Result import Result
# from fogadas import fogadas
from fuggvenyek import*
from maifogadas import maifogadas
from Resultkezi import Resultkezi
from Resultkosar import Resultkosar
from Resultvizilabda import Resultvizilabda

neveklist = []

def olvasas():
    results = []
    file = open('meccsek.csv', 'r' , encoding='utf8')
    elsosor = file.readline()

    for row in file:
        
        splitted = row.split(';')
        
        
        res = Result()
        res.date = splitted[0]
        res.hazai = splitted[1]
        res.vendeg = splitted[2]
        res.odds1 = splitted[3]
        res.odds2 = splitted[4]
        
        results.append(res)
    
    
    
    
    file.close()
    return results
    
def olvasaskezi():
    resultskezi = []
    file = open('kezimeccs.csv', 'r' , encoding='utf8')
    elsosor = file.readline()

    for row in file:
        
        splitted = row.split(';')
        
        
        res = Resultkezi()
        res.date = splitted[0]
        res.hazai = splitted[1]
        res.vendeg = splitted[2]
        res.odds1 = splitted[3]
        res.odds2 = splitted[4]
        
        resultskezi.append(res)
    
    
    
    
    file.close()
    return resultskezi

def olvasaskosar():
    resultskosar = []
    file = open('kosarlabdameccs.csv', 'r' , encoding='utf8')
    elsosor = file.readline()

    for row in file:
        
        splitted = row.split(';')
        
        
        res = Resultkosar()
        res.date = splitted[0]
        res.hazai = splitted[1]
        res.vendeg = splitted[2]
        res.odds1 = splitted[3]
        res.odds2 = splitted[4]
        
        resultskosar.append(res)
    
    
    
    
    file.close()
    return resultskosar

def olvasasvizilabda():
    resultsvizilabda = []
    file = open('vizilabdameccs.csv', 'r' , encoding='utf8')
    elsosor = file.readline()

    for row in file:
        
        splitted = row.split(';')
        
        
        res = Resultvizilabda()
        res.date = splitted[0]
        res.hazai = splitted[1]
        res.vendeg = splitted[2]
        res.odds1 = splitted[3]
        res.odds2 = splitted[4]
        
        resultsvizilabda.append(res)
    
    
    
    
    file.close()
    return resultsvizilabda

def loadData(email):
    fogadasok = []
    file = open('fogadásaim.csv', 'r' , encoding='utf8')
    
    for row in file :
        splitted = row.strip().split(";")
        if splitted[7] == email:
            print(row)
        
   
        # splitted = row.split(';')
        
        # fog = maifogadas()
        # fog.kimenet = splitted[0]
        # fog.datum = splitted[1]
        # fog.hazai = splitted[2]
        # fog.vendeg = splitted[3]
        # fog.odds1 = splitted[4]
        # fog.odds2 = splitted[5]
        
        # fogadasok.append(fog)
    
    
    
    
    file.close()
    return fogadasok
    

def signup (email, pwd):
    file = open('nevek.csv', 'r+' , encoding='utf8')
    
   
    for row in file:
        neveklist.append(row.strip())
    
    
    file.write(email + ';') 
    file.write(pwd + '\n') 
    
    file.close()
    

def login (email, pwd):
    file = open('nevek.csv', 'r' , encoding='utf8')
    
   
    for row in file:
        neveklist.append(row.strip())
    
    
    
    file.close()



