menu = ('saldo', 'sprzedaz', 'zakup', 'konto', 'lista', 'magazyn', 'przeglad', 'koniec',)
konto = 1000
historia = []
magazyn = {}
while True:
    print(f'Uzytkowniku masz dotepne nastepujace opcje : {menu}')
    wybor = str(input('Podaj wybraną opcje: \n'))
    if wybor in menu:
        if wybor == 'koniec':
            print('Zakończyłeś działanie programu!')
            break
        elif wybor == 'saldo':
            print('Wybrales saldo')
            operacja = str.lower(input('Podaj rodzaj operacji w -wpłata, p - platość:  '))
            kwota = float(input('Podaj kwotę: '))
            if operacja == 'w':
                konto += kwota
                zadanie = f"Dokonano {operacja} na kwotę {kwota}"
                historia.append(zadanie)
                print(historia)
            elif operacja == 'p' and konto >= kwota:
                konto -= kwota
                zadanie = f"Dokonano {operacja} na kwotę {kwota}"
                historia.append(zadanie)
                print(historia)
            elif operacja == 'p' and konto < kwota:
                print('Niemasz srodków na koncie')
            else:
                print('Podałes zły rodzaj operacji!!')
        elif wybor == 'sprzedaz':
            print('Wybrałeś sprzedaż produktu.')
            produkt_do_przedazy = str(input(' Podaj produkt do sprzedaży: '))
            ilosc_do_sprzedazy = float(input('Podaj ilość produktów do spredaży: '))
            if produkt_do_przedazy not in magazyn:
                print('Produktu nie ma w magazynie. Nie może zostac sprzedany.')
            if produkt_do_przedazy in magazyn:
                dane_produktu = magazyn.get(produkt_do_przedazy)
                ilosc_produktu = dane_produktu['ilosc']
                if ilosc_produktu > ilosc_do_sprzedazy:
                    cena_sprzedazy = dane_produktu['cena']
                    konto += ilosc_do_sprzedazy * cena_sprzedazy
                    ilosc_produktu -= ilosc_do_sprzedazy
                    sprzedaz_produktu = {produkt_do_przedazy: {
                        'cena zakupu': cena_sprzedazy,
                        'ilosc': ilosc_do_sprzedazy,
                    }}
                    magazyn[produkt_do_przedazy] = {'cena': cena_sprzedazy, 'ilosc': ilosc_produktu}

                    zadanie = f"Sprzedano {sprzedaz_produktu}"
                    historia.append(zadanie)

                elif ilosc_produktu == ilosc_do_sprzedazy:
                    cena_sprzedazy = dane_produktu['cena']
                    konto += ilosc_do_sprzedazy * cena_sprzedazy
                    ilosc_produktu -= ilosc_do_sprzedazy
                    sprzedaz_produktu = {produkt_do_przedazy: {
                        'cena zakupu': cena_sprzedazy,
                        'ilosc': ilosc_do_sprzedazy,
                    }}
                    del magazyn[produkt_do_przedazy]

                    zadanie = f"Sprzedano {sprzedaz_produktu}"
                    historia.append(zadanie)
                else:
                    print(f'Na stanie magazynu nie ma wystarczającej ilości produktu.\n'
                          f' W magazynie jest {ilosc_produktu}')

        elif wybor == 'zakup':
            print('Wybrałeś zakup produktu.')
            produkt = str(input('Podaj nazwę produktu: '))
            cena_zakupu = float(input('Podaj cenę produktu: '))
            ilosc = float(input('Podaj ilosc produktów: '))
            if cena_zakupu <= 0:
                print('Podano niewłaściwą cenę zakupu!')
            elif cena_zakupu * ilosc <= konto:
                if produkt in magazyn:
                    konto -= cena_zakupu * ilosc
                    zakup_produktu = {produkt: {
                        'cena zakupu': cena_zakupu,
                        'ilosc': ilosc,
                    }}
                    ilosc += ilosc
                    magazyn[produkt] = {'cena': cena_zakupu, 'ilosc': ilosc}

                    zadanie = f"zakupiono {zakup_produktu}"
                    historia.append(zadanie)

                else:
                    zakup_produktu = {produkt: {
                        'cena zakupu': cena_zakupu,
                        'ilosc': ilosc,
                    }}
                    magazyn[produkt] = {'cena': cena_zakupu, 'ilosc': ilosc}
                    konto -= cena_zakupu * ilosc

                    zadanie = f"zakupiono {zakup_produktu} "
                    historia.append(zadanie)

            else:
                print('Nie masz wystarczających środków na koncie na zakup produktu.')
        elif wybor == 'konto':
            print('Wybrales sprawdzenie stanu konta firmowego.')
            print(f'Stan konta firmowego wynosi: [{konto}]')
        elif wybor == 'lista':
            print('Wybrales sprawdzenie stanu magazynu')
            for k, v in magazyn.items():
                print(f'{k} - {v}')
            # import pprint
            # pprint.pprint(magazyn, indent=2)
        elif wybor == 'magazyn':
            print('Wybrałeś magazyn.\n'
                  'Lista produktów znajdująca sie w magazynie:')
            for k in magazyn.keys():
                print(f'{k}')
            wybrany_produkt = str(input('Podaj nazwę wybranego produktu: '))
            if wybrany_produkt not in magazyn:
                print('Wybranego produktu nie ma w magazynie')
            else:
                print(f'Stan dla wybranego produktu: {wybrany_produkt} - {magazyn[wybrany_produkt]}')
        elif wybor == 'przeglad':
            print('przeglad')

    else:
        print('Podales nieprawidlowa opcje!')
