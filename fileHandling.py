from Result import Result


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
        
        results.append(res)
    
    
    
    
    file.close()
    return results
    



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

def saveResult(res):
    file = open('fogadásaim.csv','a',encoding='utf8')
    file.write(f'{res.date};{res.hazai};{res.vendeg}')