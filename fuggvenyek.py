from fileHandling import*

from fogadas import fogadas


results = olvasas()

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
    
  

def searchByName(results, csapatnev):
    for item in results:
        if item.hazai == csapatnev or item.vendeg == csapatnev: 
            print(f'{item.date} - {item.hazai} - {item.vendeg}')


def searchByName2(results, csapatnev, tipp):
  
    for item in results:
        if item.hazai == csapatnev or item.vendeg == csapatnev: 
            print(f'{item.date} - {item.hazai} - {item.vendeg}')
            file = open('fogadásaim.csv','a',encoding='utf8')
            file.write( tipp + ';' + item.date + ';' + item. hazai + ';' + item.vendeg + '\n')
            file.close() 
            return
        else : 
            print('nincs ilyen csapat')
      


    
def foci(osszesadat):
    print('1 - meccs keresése')
    print('2 - a nap fogadása')
    print('3 - biztos mix')
    print('4 - magas oddsok')
    valertek = input('adja meg a  :')
    if valertek == '1':
        print('1 - keresés csapat alapján')
        print('2 - keresés időpont alapján')
        valasztottertek = int(input('adja meg a választott funkció számát :'))
        if valasztottertek == 1:
            csapatnev = input('adja meg a csapat nevét:')
            searchByName(results, csapatnev)
            print('tippeljen ')
            print('1 - hazai')
            print('2 - vendeg')
            print('x - döntetlen')
            tipp = input('választott kimenet :')
            searchByName2(results, csapatnev, tipp)
            
            
    else : 
        pass

        
       
    
# def saveResult(tipp, name):
#     file = open('fogadásaim.csv','a',encoding='utf8')
#     file.write(f'{tipp};{name} \n')

#     file.close()

        
            
       
    # elif valasztottertek == 2:
    #     idopont = input('adja meg a mérközés időpontját :')
    #     if idopont not in data:
    #         print('nincs ilyen idopont')
    #     else:
    #        for row in data:
    #             print(row)
    
