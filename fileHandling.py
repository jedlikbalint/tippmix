from footballResult import*


def loadData():
    
    footballresults = []
    f = open('meccsek.csv', 'r', encoding='utf8')
    
    f.readline()
    
    for row in f:
        
        splitted = row.split(';')
        
        
        res = footballResult()
        res.idopont = splitted[0]
        res.hazai = splitted[1]
        res.vendeg = splitted[2]
        
    
        footballresults.append(res)
    
    f.close
    
    return footballresults

