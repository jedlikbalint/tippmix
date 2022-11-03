from menu import*
from fuggvenyek import*
print(' Üdvözlünk')



choice = -1
while choice != 0:
    choice = menu()
    if choice == 1:
        befizetés()
    elif choice == 2:
        kifizetés(befizetés)
    
    