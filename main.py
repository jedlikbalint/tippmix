from menu import*
from fuggvenyek import*



print(' Üdvözlünk')
print(f'{egyenleg}')
print(menu())


    
choice = -1
while choice != 0:
    choice = menu()
    if choice == 1:
        befizetés(egyenleg)
        print(f'{egyenleg}')
    elif choice == 2:
        kifizetés(egyenleg)
        
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