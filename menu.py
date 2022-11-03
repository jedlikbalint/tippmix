from fuggvenyek import*

def menu():
    print('Kérem válasszon a lehetőségek közül ')
    print('1 - befizetés')
    print('2 - kifizetés')
    print('3 - mai meccsek')
    print('4 - fogadásaim')
    print('0 - kilépés')

    menu = input('a választott funkció száma :')
    
    if menu == '1':
        befizetés()
