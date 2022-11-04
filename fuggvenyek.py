

def befizetés(feltoltott):
    egyenleg = 0
    osszeg = 0
    
    
    
    osszeg = feltoltott + egyenleg
    
    return osszeg
    
        
def kifizetés(osszeg):
    
    
    if osszeg == 0:
        print('Önnek nincs pénz az egyenlegén , sajnos nem tud mit kivenni .')
    elif osszeg > 0:
        kifizetett = int(input('Mennyit szeretne kivenni  : ')) 
        if kifizetett > 0:
            osszeg = osszeg - kifizetett
            print(f'az ön új egyenlege : {osszeg} ft')
        else: 
            print('ön érvénytelen összeget adott meg !')
    return osszeg
    
    