from fileHandling import*

from fogadas import fogadas


results = olvasas()
egyenleg = 0

def befizetés(feltoltott):
    global egyenleg
    egyenleg += feltoltott

def egyenlegLekerdezes():
    return egyenleg
        
def kifizetés():
    global egyenleg
    if egyenleg == 0:
        print('Önnek nincs pénz az egyenlegén , sajnos nem tud mit kivenni .')
    elif egyenleg > 0:
        kifizetett = int(input('Mennyit szeretne kivenni  : ')) 
        if kifizetett < egyenleg:
            egyenleg = egyenleg - kifizetett
            print(f'az ön új egyenlege : {egyenleg} ft')
        else: 
            print('nincs ennyi az egyenlegén!')

    
def egyenlegFogadas(tet):
    global egyenleg
    egyenleg -= int(tet)
     

def searchByName(results, csapatnev):
    for item in results:
        if item.hazai == csapatnev or item.vendeg == csapatnev: 
            print(f'{item.date} - {item.hazai} - {item.vendeg}')

def idopontkeres(results, idopont):
    for item in results:
        if item.date == idopont:
            print(f'{item.date} - {item.hazai} - {item.vendeg}')


def searchByName2(results, csapatnev, tipp, tet):
  
    for item in results:
        if item.hazai == csapatnev or item.vendeg == csapatnev: 
            email = input('add meg az emailcimedet : ')
            file = open('fogadásaim.csv','a',encoding='utf8')
            file.write( tipp + ';' + str(tet) + ';' + item.date + ';' + item. hazai + ';' + item.vendeg + ';' + item.odds1 + ';' + item.odds2 + ';' + email + '\n')
            file.close() 
        
      
def kombinaltkotes(tet, tipp, kombinalt):
    file = open('fogadásaim.csv','a',encoding='utf8')
    file.write( tipp + ';' + tet + ';' + kombinalt + '\n')
    file.close() 
    

def minOdds(results):
    for item in results:
        if float(item.odds1) < 1.3 or float(item.odds2) < 1.3 :
            print(f'{item.date} - {item.hazai} - {item.vendeg} - {item.odds1} - {item.odds2}')
            
         
def maxprinnt(results):
    for item in results:
        if float(item.odds1) > 3 or float(item.odds2) > 3 :
            print(f'{item.date} - {item.hazai} - {item.vendeg} - {item.odds1} - {item.odds2}')
   
def maxOdds(results, tipp, tet):
    list = []
    for item in results:
        if float(item.odds1) > 3 or float(item.odds2) > 3 :
            print(f'{item.date} - {item.hazai} - {item.vendeg} - {item.odds1} - {item.odds2}')
            
            list.append(item.date + ';' + item.hazai + ';' + item.vendeg + ';' + item.odds1 + ';' + item.odds2 )
    print(list)
    email = input('add meg az emailcimedet : ')
    file = open('fogadásaim.csv','a',encoding='utf8')
    for item in list:
        file.write(f'{tipp};{str(tet)};{item};{email}\n')
    file.close() 
    

    
def foci(osszesadat):
    global egyenleg
    print('1 - meccs keresése')
    print('2 - a nap fogadása')
    print('3 - biztos mix')
    print('4 - magas oddsok')
    valertek = input('adja meg a  :')
    print('----------------------------------------')
    if valertek == '1':
        print('1 - keresés csapat alapján')
        print('2 - keresés időpont alapján')
        valasztottertek = int(input('adja meg a választott funkció számát :'))
        print('--------------------------------------------')
        if valasztottertek == 1:
            csapatnev = input('adja meg a csapat nevét:')
            searchByName(results, csapatnev)
            print('tippeljen ')
            print('1 - hazai')
            print('2 - vendeg')
            print('x - döntetlen')
            tipp = input('választott kimenet :')
            tet = input('adja meg az összeget :')
            egyenlegFogadas(tet)
            print(f'Új egyenleg: {egyenleg}')
            
            print('----------------------------------------------')
            searchByName2(results, csapatnev, tipp, tet)
        elif valasztottertek == 2:
            idopont = input('adja meg az idopontot : ')
            idopontkeres(results, idopont)
            print('tippeljen ')
            print('1 - hazai')
            print('2 - vendeg')
            print('x - döntetlen')
            tipp = input('választott kimenet :')
            tet = input('adja meg az összeget :')
            egyenlegFogadas(tet)
            print(f'Új egyenleg: {egyenleg}')
            
            print('----------------------------------------------')
            searchByName2(results, csapatnev, tipp, tet)
    elif valertek == '3':   
            minOdds(results)
            print('tippeljen ')
            print('1 - hazai')
            print('2 - vendeg')
            print('x - döntetlen')
            tipp = input('választott kimenet :')
            tet = input('adja meg az összeget :')
            searchByName2(results, tipp, tet)
            
            
    elif valertek == '4':
        maxprinnt(results)
        tipp = input('választott kimenet :')
        tet = input('adja meg az összeget :')
        maxOdds(results, tipp, tet)
    
        
         
          
            
    else : 
        print('rossz értéket adott meg !!!')

        
       
    
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
    
