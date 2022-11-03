def befizetés():
    befizetettOsszeg = 0
    print(f'Elkölthető összeg : {befizetettOsszeg} ft' )
    feltoltott = int(input('feltölteni kivánt összeg : '))
    if feltoltott != 0 and feltoltott > 0 :
        befizetettOsszeg += feltoltott
        print(f'Elkölthető összeg : {befizetettOsszeg} ft')
    else : 
        print('ön érvénytelen összeget adott meg !')
    return befizetettOsszeg
        
def kifizetés(befizetettOsszeg):
    kifizetettOsszeg = 0
    print(f'Elkölthető összeg : {befizetettOsszeg} ft' )
    if befizetettOsszeg == 0:
        print('Önnek nincs pénz az egyenlegén , sajnos nem tud mit kivenni .')
    elif befizetettOsszeg > 0:
        kifizetett = int(input('Mennyit szeretne kivenni  : ')) 
        if kifizetett > 0:
            befizetettOsszeg - kifizetett
            print(f'az ön új egyenlege : {befizetettOsszeg} ft')
        else: 
            print('ön érvénytelen összeget adott meg !')
    return befizetettOsszeg
    
    