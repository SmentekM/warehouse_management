from klasa_manager import manager

menu = ('saldo', 'sprzedaz', 'zakup', 'konto', 'lista', 'magazyn', 'przeglad', 'koniec',)

manager.execute('wczytanie_plikow')
while True:
    print(f'Uzytkowniku masz dotepne nastepujace opcje : {menu}')
    wybor = str(input('Podaj wybraną opcje: \n'))

    if wybor == 'koniec':
        print('Zakończyłeś działanie programu!')
        break

    else:
        manager.execute(wybor)

manager.execute('zapisz_w_pliku')
