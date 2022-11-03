from menu import*
from fuggvenyek import*
print(' Üdvözlünk')



choice = -1
while choice != 0:
    choice = menu()
    if choice == 1:
        befizetés(egyenleg)
        if befizetés() > 0:
            print(f'Elkölthető összeg : {befizetés()} ft')
        else : 
            print('ön érvénytelen összeget adott meg !')
    
    elif choice == 2:
        kifizetés(befizetés)
    
    