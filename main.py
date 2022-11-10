from menu import*
from fuggvenyek import*
from fileHandling import*


print(' Üdvözlünk')




    
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
        print('A - mai meccsek')
        print('B - szelvény ajánló')
        valasztas = input('Kérem válasszon egy opciót ( A vagy B )').upper()
        if valasztas == 'A':
            print('Válasszon sportágat :')
            print('1 - Labdarugás')
            print('2 - Kézilabda')
            print('3 - vizilabda')
            print('4 - Kosárlabda')
            sportag = input('A választott sportág száma :')
            if sportag == '1':
                foci()
            elif sportag == '2':
                pass
            elif sportag == '3':
                pass
            elif sportag == '4':
                pass
        elif valasztas == 'B':
            pass
            
    #     uj(nev)
    # elif choice == 4:
    #     nev = input('Add meg melyik nevet kell kitörölni  : ')
    #     torles(nev)
    # elif choice == 5:
    #     nev = input('Add meg melyik nevet kell modosítani  : ')
    #     ujnev = input('Add meg mire  : ')
    #     modosit(nev, ujnev)