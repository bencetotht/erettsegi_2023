#!/usr/bin/env python3

# A feladatban remekül megfigyelhető a tizedes törtek lebegőpontos ábrázolásából
# eredő pontatlanság. Ha ezt programozóként nem engedhetjük meg magunknak,
# akkor a float adattípus helyett a decimal modul típusait érdemes használni.

def futamot_kiértékel(futam):
    előjel = futam[0]
    szám = float(''.join(futam[1:]))
    # Csak tesztelés alatt fontos:
    # print(f'{ciszterna_tartalma=}, {előjel}{szám}', end=' ')
    if előjel == '+':
        return szám
    else:
        return -1*szám


with open('vizek.txt') as forrásfájl:
    # Később a k változóban tároljuk a beolvasott karaktereket.
    # Most azért kapja a True értéket, hogy belépjünk a ciklusba.
    k = True
    fél_icce_alatti = False
    futam = [] # ebben tároljuk a beolvasott karaktereket a következő előjelig
    ciszterna_tartalma = 52.47 # a feladat szövege alapján
    előjel = None
    előző_előjel = None
    max_pluszjelek = 0
    pluszjelek = 0
    legnagyobb_tömlő = 0
    while k:
        k = forrásfájl.read(1)
        # Használhatnánk a rozmár-operátort (walrus-operator)
        # az előző két sor egyesítésére:
        # while k := forrásfájl.read(1)
        if k: # ha volt mit beolvasni (tartott még a fájl)
            if k == '+' or k == '-': # új futam kezdődik a fájlban
                # először a leghosszabb pluszjelsorozattal foglalkozunk
                if k == '-':
                    if előző_előjel == '+':
                        if pluszjelek > max_pluszjelek:
                            max_pluszjelek = pluszjelek
                            # Csak tesztelés alatt fontos:
                            # print(f'Új legjosszabb pluszjelsorozat: {max_pluszjelek}.')
                        pluszjelek = 0
                else: # azaz + jelet olvastunk
                    pluszjelek += 1
                előző_előjel = k
                # aztán a futam kiértékelése kerül sorra
                if futam: # ha nem ez az első futam, kiértékeljük az előző futamot
                    víz = futamot_kiértékel(futam)
                    ciszterna_tartalma += víz
                    if ciszterna_tartalma < 0.5: # b. feladathoz
                        fél_icce_alatti = True
                    if abs(víz) > legnagyobb_tömlő: # d. feladathoz, az a tömlő is lehet legnagyobb, amelyikkel kivettek vizet
                        legnagyobb_tömlő = abs(víz)
                # új futamot kezdünk
                futam = [k]
            else:
                futam += k
            # Csak tesztelés alatt fontos:
            # print(''.join(futam))
    # Ha már nem sikerült újabb karaktert olvasni, akkor kilépünk a
    # while-ciklusból, de még az utolsó futamot nem értékeltük ki.
    víz = futamot_kiértékel(futam)
    ciszterna_tartalma += víz
    # Az alábbi három if-ág jelentőségének szemlétetését érdemes a
    # vizek_masik_adatsor_az_utolso_pillanatban_beallo_valtozasok_szemleletetesere.txt
    # fájllal tesztelni a programot.
    if ciszterna_tartalma < 0.5: # b. feladathoz, a végén is lehet a legkevesebb víz
        fél_icce_alatti = True
    if abs(víz) > legnagyobb_tömlő: # d. feladathoz, az a utolsó tömlő is lehet a legnagyobb
        legnagyobb_tömlő = abs(víz)
    if pluszjelek > max_pluszjelek: # c. feladathoz, az utolso +sorozat is lehet a leghosszabb
        max_pluszjelek = pluszjelek

# 1. feladat
print(f'A megfigyelt időszak végén {ciszterna_tartalma} icce víz van a ciszternában.')
# 2. feladat
print(f'{"Volt" if fél_icce_alatti else "Nem volt"} fél iccénél kevesebb víz a ciszternában.')
# 3. feladat
print(f'A legtöbb, vízkivét nélküli egymást követő vízbetöltések száma: {max_pluszjelek}.')
# 4. feladat
print(f'A legnagyobb tömlő {legnagyobb_tömlő} iccés.')
# 5. feladat
print(f'{ciszterna_tartalma // 6:.0f} akváriumot lehet megtölteni a ciszterna vizével.')
