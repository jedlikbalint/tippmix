from menu import*
from fuggvenyek import*
from fileHandling import*
from kezifuggveny import*
from kosarfuggveny import*
from vizilabdafuggveny import*

osszesadat = olvasas()

# fogadat = loadData()
results = olvasas()
print(' Üdvözlünk')


def reg(): 
    email = input("Adja meg az e-mail címet: ") 
    pwd = input("Adja meg a jelszót: ") 
    conf_pwd = input("Jelszó megerősítése: ")
    if conf_pwd == pwd: 
        signup(email, pwd) 
        print('Sikeres regisztráció!')
    else: 
        print ("A jelszó nem ugyanaz, mint fent! \n")
        
def bejel(): 
   
    email = input('Adja meg az e-mail címet: ')
    pwd = input('Adja meg a jelszót: ')
   
    login(email, pwd)
    for row in neveklist:
        splitted =row.split(';')
    
    if email == splitted[0] and pwd == splitted[1]:
        print('Sikeres bejelentkezés !')
        choice = -1
        while choice != 0:
            choice = menu()
            print('--------------------------------------------------')
            
            if choice == 1:
                feltoltott = int(input('feltölteni kivánt összeg : '))
                print(f'Elkölthető összeg : {befizetés(feltoltott)} ft' )
            elif choice == 2:
                print(f'Elkölthető összeg : {egyenlegLekerdezes()} ft' )
                kifizetés()
            elif choice == 3:
             
                print('Válasszon sportágat :')
                print('1 - Labdarugás')
                print('2 - Kézilabda')
                print('3 - vizilabda')
                print('4 - Kosárlabda')
                sportag = input('A választott sportág száma :')
                print('-----------------------------------------')
                if sportag == '1':
                    foci(osszesadat)
                elif sportag == '2':
                    kezi(osszesadat)
                elif sportag == '3':
                    vizilabda(osszesadat)
                elif sportag == '4':
                    kosar(osszesadat)
                
                
            elif choice == 4 :
                email = input('add meg az emailcimedet : ')
                print(loadData(email))
    else:
         print('Sikertelen bejelentkezés ! \n')
while 1: 
    print("********** Bejelentkezési rendszer **********") 
    print("1.Regisztráció") 
    print("2.Bejelentkezés") 
   
    ch = int(input("Válassz a funikciók közül: "))
    if ch == 1:
        reg()
    elif ch == 2:
        bejel()
    else:
        print("Rossz érték !")


    
choice = -1
while choice != 0:
    choice = menu()
    print('----------------------------')
    if choice == 1:
        feltoltott = int(input('feltölteni kivánt összeg : '))
        print(f'Elkölthető összeg : {befizetés(feltoltott)} ft' )
    elif choice == 2:
        print(f'Elkölthető összeg : {befizetés(feltoltott)} ft' )
        kifizetés(befizetés(feltoltott))
    elif choice == 3:
        
        
        print('Válasszon sportágat :')
        print('1 - Labdarugás')
        print('2 - Kézilabda')
        print('3 - vizilabda')
        print('4 - Kosárlabda')
        sportag = input('A választott sportág száma :')
        if sportag == '1':
            foci(osszesadat)
        elif sportag == '2':
            kezi(osszesadat,)
        elif sportag == '3':
            pass
        elif sportag == '4':
            pass
        else:
            print("Rossz érték !")
   
        
            
    #     uj(nev)
    # elif choice == 4:
    #     nev = input('Add meg melyik nevet kell kitörölni  : ')
    #     torles(nev)
    # elif choice == 5:
    #     nev = input('Add meg melyik nevet kell modosítani  : ')
    #     ujnev = input('Add meg mire  : ')
    #     modosit(nev, ujnev)
    