from footballResult import*


def loadData():
    
    footballResults = []
    f = open('meccsek.csv', 'r', encoding='utf8')
    
    f.readline()
    
    for row in f:
        
        splitted = row.split(';')
        
        
        res = footballResults()
        res.idopont = splitted[0]
        res.hazai = splitted[1]
        res.vendeg = splitted[2]
        
    
        footballResults.append(res)
    
    f.close
    
    return footballResults

