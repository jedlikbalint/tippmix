from menu import*
from fuggvenyek import*



print(' Üdvözlünk')




    
choice = -1
while choice != 0:
    choice = menu()
    if choice == 1:
        feltoltott = int(input('feltölteni kivánt összeg : '))
        print(f'Elkölthető összeg : {befizetés(feltoltott)} ft' )
    elif choice == 2:
        print(f'Elkölthető összeg : {befizetés(feltoltott)} ft' )
        kifizetés(befizetés(feltoltott))
        
    # elif choice == 3:
    #     nev = input('Add meg az új nevet : ')
    #     uj(nev)
    # elif choice == 4:
    #     nev = input('Add meg melyik nevet kell kitörölni  : ')
    #     torles(nev)
    # elif choice == 5:
    #     nev = input('Add meg melyik nevet kell modosítani  : ')
    #     ujnev = input('Add meg mire  : ')
    #     modosit(nev, ujnev)