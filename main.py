from menu import*
from fuggvenyek import*
from fileHandling import*
import hashlib

print(' Üdvözlünk')


def signup(): 
    email = input("Adja meg az e-mail címet: ") 
    pwd = input("Adja meg a jelszót: ") 
    conf_pwd = input("Jelszó megerősítése: ")
    if conf_pwd == pwd: 
        enc = conf_pwd.encode() 
        hash1 = hashlib.md5(enc).hexdigest()
        with open('nevek.txt', 'w') as f: 
             f.write(email + '\n') 
             f.write(hash1) 
        f.close() 
        print('Sikeres regisztráció!')
    else: 
        print ("A jelszó nem ugyanaz, mint fent! \n")
def login(): 
    email = input("Adja meg az e-mail címet: ") 
    pwd = input("Adja meg a jelszót: ") 
    conf_pwd = input("Jelszó megerősítése: ")
    if conf_pwd == pwd: 
        enc = conf_pwd.encode() 
        auth_hash = hashlib.md5(enc).hexdigest()
        with open('nevek.txt', 'w') as f:  
            stored_email, stored_pwd = f.read().split("\n" ) 
    f.close()
    if email == stored_email and auth_hash == stored_pwd: 
         print("Sikeresen bejelentkezett!") 
    else: 
         print("A bejelentkezés sikertelen! \n")
while 1: 
    print("********** Bejelentkezési rendszer **********") 
    print("1.Regisztráció") 
    print("2.Bejelentkezés") 
    print("3 .Kilép !")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")


    
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