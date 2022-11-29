from fuggvenyek import*


def menu():
    option = -1
    while option < 0 or option > 4 : 
        print('Kérem válasszon a lehetőségek közül ')
        print('1 - befizetés')
        print('2 - kifizetés')
        print('3 - meccsek')
        print('4 - fogadásaim')
        print('0 - kilépés')

        option = int(input('a választott funkció száma :'))
    return option



