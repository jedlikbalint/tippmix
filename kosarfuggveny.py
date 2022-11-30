from fileHandling import*

from fogadas import fogadas


resultskosar = olvasaskosar()

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
     

def searchByName(resultskosar, csapatnev):
    for item in resultskosar:
        if item.hazai == csapatnev or item.vendeg == csapatnev: 
            print(f'{item.date} - {item.hazai} - {item.vendeg}')
            
lista = []
def idopontkeres(resultskosar, idopont):
    global lista
    for item in resultskosar:
        if item.date == idopont:
            lista.append(item.date + ';' + item.hazai + ';' + item.vendeg + ';' + item.odds1 + ';' + item.odds2 )
    print(lista)
    

def datumfogad( email, tet, tipp): 
    global lista       
    file = open('fogadásaim.csv','a',encoding='utf8')
    for item in lista:
        file.write(f'{tipp};{str(tet)};{item};{email}\n')
    file.close()


def searchByName2(resultskosar, csapatnev, tipp, tet):
  
    for item in resultskosar:
        if item.hazai == csapatnev or item.vendeg == csapatnev: 
            email = input('add meg az emailcimedet : ')
            file = open('fogadásaim.csv','a',encoding='utf8')
            file.write( tipp + ';' + str(tet) + ';' + item.date + ';' + item. hazai + ';' + item.vendeg + ';' + item.odds1 + ';' + item.odds2 + ';' + email + '\n')
            file.close() 
        
      

            
      
def kombinaltkotes(tet, tipp, kombinalt):
    file = open('fogadásaim.csv','a',encoding='utf8')
    file.write( tipp + ';' + tet + ';' + kombinalt + '\n')
    file.close() 
    
def minoddsprint(resultskosar):
    for item in resultskosar:
        if float(item.odds1) > 3 or float(item.odds2) > 3 :
            print(f'{item.date} - {item.hazai} - {item.vendeg} - {item.odds1} - {item.odds2}')

def minOdds(resultskosar,tipp, tet):
    list = []
    for item in resultskosar:
        if float(item.odds1) < 1.3 or float(item.odds2) < 1.3 :
            print(f'{item.date} - {item.hazai} - {item.vendeg} - {item.odds1} - {item.odds2}')
            list.append(item.date + ';' + item.hazai + ';' + item.vendeg + ';' + item.odds1 + ';' + item.odds2 )
    print(list)
    email = input('add meg az emailcimedet : ')
    file = open('fogadásaim.csv','a',encoding='utf8')
    for item in list:
        file.write(f'{tipp};{str(tet)};{item};{email}\n')
    file.close() 
            
         
def maxprinnt(resultskosar):
    for item in resultskosar:
        if float(item.odds1) > 3 or float(item.odds2) > 3 :
            print(f'{item.date} - {item.hazai} - {item.vendeg} - {item.odds1} - {item.odds2}')
   
def maxOdds(resultskosar, tipp, tet):
    list = []
    for item in resultskosar:
        if float(item.odds1) > 3 or float(item.odds2) > 3 :
            print(f'{item.date} - {item.hazai} - {item.vendeg} - {item.odds1} - {item.odds2}')
            
            list.append(item.date + ';' + item.hazai + ';' + item.vendeg + ';' + item.odds1 + ';' + item.odds2 )
    print(list)
    email = input('add meg az emailcimedet : ')
    file = open('fogadásaim.csv','a',encoding='utf8')
    for item in list:
        file.write(f'{tipp};{str(tet)};{item};{email}\n')
    file.close() 
    

    
def kosar(osszesadat):
    global egyenleg
    global lista
    print('1 - meccs keresése')
    print('2 - biztos mix')
    print('3 - magas oddsok')
    valertek = input('adja meg a  :')
    print('----------------------------------------')
    if valertek == '1':
        print('1 - keresés csapat alapján')
        print('2 - keresés időpont alapján')
        valasztottertek = int(input('adja meg a választott funkció számát :'))
        print('--------------------------------------------')
        if valasztottertek == 1:
            csapatnev = input('adja meg a csapat nevét:')
            searchByName(resultskosar, csapatnev)
            print('tippeljen ')
            print('1 - hazai')
            print('2 - vendeg')
            print('x - döntetlen')
            tipp = input('választott kimenet :')
            tet = input('adja meg az összeget :')
            egyenlegFogadas(tet)
            print(f'Új egyenleg: {egyenleg}')
            
            print('----------------------------------------------')
            searchByName2(resultskosar, csapatnev, tipp, tet)
        elif valasztottertek == 2:
            idopont = input('adja meg az idopontot : ')
            idopontkeres(resultskosar, idopont)
            print('tippeljen ')
            print('1 - hazai')
            print('2 - vendeg')
            print('x - döntetlen')
            tipp = input('választott kimenet :')
            tet = input('adja meg az összeget :')
            email = input('add meg az emailcimedet : ')
            datumfogad(email, tet, tipp)
            egyenlegFogadas(tet)
            print(f'Új egyenleg: {egyenleg}')
            
            print('----------------------------------------------')
            # searchByName2(results, csapatnev, tipp, tet)
    elif valertek == '2':   
            minoddsprint(resultskosar)
            tipp = input('választott kimenet :')
            tet = input('adja meg az összeget :')
            minOdds(resultskosar, tipp, tet)
            
            
    elif valertek == '3':
        maxprinnt(resultskosar)
        tipp = input('választott kimenet :')
        tet = input('adja meg az összeget :')
        maxOdds(resultskosar, tipp, tet)
    
        
         
          
            
    else : 
        print('rossz értéket adott meg !!!')
