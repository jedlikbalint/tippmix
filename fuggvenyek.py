egyenleg = 0

def befizetés(egyenleg):
    
    ujegyenleg = 0
    print(f'Elkölthető összeg : {egyenleg} ft' )
    feltoltott = int(input('feltölteni kivánt összeg : '))
    if  feltoltott < 0 :
        print('érvénytelen összeg !!')
        
    else:
        osszeg = egyenleg + ujegyenleg
    
    return osszeg
    
        
# def kifizetés(egyenleg):
    
#     print(f'Elkölthető összeg : {egyenleg} ft' )
#     if egyenleg == 0:
#         print('Önnek nincs pénz az egyenlegén , sajnos nem tud mit kivenni .')
#     elif egyenleg > 0:
#         kifizetett = int(input('Mennyit szeretne kivenni  : ')) 
#         if kifizetett > 0:
#             egyenleg = egyenleg - kifizetett
#             print(f'az ön új egyenlege : {egyenleg} ft')
#         else: 
#             print('ön érvénytelen összeget adott meg !')
#     return egyenleg
    
    