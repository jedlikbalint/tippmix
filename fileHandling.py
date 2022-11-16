data = []
neveklist = []

def olvasas():
    file = open('meccsek.csv', 'r' , encoding='utf8')
    elsosor = file.readline()

    
    for row in file:
        data.append(row.strip())
    
    
    file.close()
    return data
    


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

