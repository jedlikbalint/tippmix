data = []

def olvasas():
    file = open('meccsek.csv', 'r' , encoding='utf8')
    
    elsosor = file.readline()
    # masodik = file.readline()
    
    
    
    print(elsosor)
    
    
    
    for row in file:
        data.append(row.strip())
    
    
    
    
    # print(masodik)
    
    file.close()
    





