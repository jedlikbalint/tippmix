egyenleg = 0

def befizetés(egyenleg):
    
   
    print(f'Elkölthető összeg : {egyenleg} ft' )
    feltoltott = int(input('feltölteni kivánt összeg : '))
    if  feltoltott > 0 :
        egyenleg += feltoltott
    return egyenleg
    
        
def kifizetés(befizetettOsszeg):
    kifizetettOsszeg = 0
    print(f'Elkölthető összeg : {befizetettOsszeg} ft' )
    if befizetettOsszeg == 0:
        print('Önnek nincs pénz az egyenlegén , sajnos nem tud mit kivenni .')
    elif befizetettOsszeg > 0:
        kifizetett = int(input('Mennyit szeretne kivenni  : ')) 
        if kifizetett > 0:
            kifizetettOsszeg = befizetettOsszeg - kifizetett
            print(f'az ön új egyenlege : {befizetettOsszeg} ft')
        else: 
            print('ön érvénytelen összeget adott meg !')
    return befizetettOsszeg
    
    