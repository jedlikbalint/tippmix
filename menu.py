from fuggvenyek import*


def menu():
    option = -1
    while option < 0 or option > 4 : 
        print('0 - kilépés')
        print('1 - befizetés')
        print('2 - kifizetés')
        print('3 - mai meccsek')
        print('4 - fogadásaim')
        
        option =  int(input('Válosszon a fentiek közül : '))
    return option
    
   
   
    
    
    