

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
    
    
    
    
def foci(footballresults):
    print('1 - meccs keresése')
    print('2 - a nap fogadása')
    print('3 - biztos mix')
    print('4 - magas oddsok')
    valasztas = input('adja meg a választott funkció számát :')
    if valasztas == 1:
        print('1 - keresés csapat alapján')
        print('2 - keresés időpont alapján')
        valasz = input('adja meg a választott funkció számát :')
        if valasz == 1:
            csapatnev = input('adja meg a csapat nevét:')
            
        elif valasz == 2:
            idopont = input('adja meg a mérközés időpontját :')
    
    