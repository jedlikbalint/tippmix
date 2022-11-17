from Eredmenyek import Eredmenyek
neveklist = []





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




def olvasas():
    file = open('meccsek.csv', 'r' , encoding='utf8')
    results = []
    
    
    file.readline()
    
    for row in file:
        e = Eredmenyek()
        splitted = row.strip().split(';')
        e.evszam = str(splitted[0])
        e.hazai = str(splitted[1])
        e.vendeg = str(splitted[2])
        
        results.append(e)
        
    file.close()
    return results
    


