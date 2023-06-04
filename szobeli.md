## Szövegszerkesztés
### Betűtípusok és bekezdések
>**betűtípus:** azonos grafikai elvek szerint megtervezett ábécé
- formai szempontból három fő kategóriába sorolhatjuk:
	- **talpas betűk**: vonalvastagsága változó, a szárak talpakban végződnek
	- **talp nélküli betűtípusok**: nem rendelkeznek talpakkal, vonalvastagságuk sok esetben állandó
	- **dísz- vagy reklámbetűk**
- Egy adott betűtípus változatait betűstílusoknak nevezzük (félkövér, dőlt, félkövér dőlt, aláhúzott, felső index, kiskapitális)
- A betűk méretének egysége a pont

- A bekezdéseket a bekezdésjelek (¶) határolják
-  leggyakoribb bekezdésformátumok: igazítás, behúzás, térköz és sorköz
> **igazítás**: a bekezdés sorainak egymáshoz viszonyított helyzete
> **behúzás**: a bekezdés sorainak távolsága a margótól
> **térköz**: a bekezdés távolsága az előző, illetve következő bekezdéstől
> **sorköz**: a bekezdés sorainak távolsága
- egyéb formázások: pl iniciálé, háttérszín, szegély

### Táblázatok és tabulátorok
- táblázatok formázása: szélesség, magasság, szegélyek, háttészín, cellák tartalmának igazítása, margók, cellaköz, cellák felosztása / egyesítése

### Oldalbeállítások, fájlműveletek
- nyelvi beállítások:
	- nyelvi ellenőrzés
	- elválasztás
- oldalbeállítások:
	- papír mérete
	- tájolása
	- margók nagysága
> **szövegtükör**: margók által határolt területet

### Kördokumentum
> **kördokumentum**: több címzett számára lényegében azonos tartalommal elkészített, de egyedi adatokkal kiegészített dokumentumhalmaz
- lépései: adatforrás (táblázat, amelynek első sora tartalmazza a mezőneveket) megadása, **törzsdokumentum** elkészítése, egyesítésük

### Nagy dokumentumok formázása
> **bekezdésstílus**: egy adott bekezdésre vonatkozó beállítások összessége, amelyet a stílus nevével azonosítunk
- stílusok hierarchikus rendszert alkotnak, amelyben egyes formázási beállítások öröklődnek, illetve felüldefiniálhatók
- tartalomjegyzék elkészítéséhez kellenek a címsorok

- élőfej, élőláb eltérhet dokumentum páros és páratlan oldalain
> **lábjegyzet**: az olvasó számára szolgáló kiegészítés, amelyet a dokumentum egy adott pontjához kapcsolva általában a szövegtükör alján helyeznek el
> *Néha ezeket a kiegészítéseket egyben, a dokumentum végére teszik, ilyenkor **végjegyzetről** beszélünk*

> **szakasz** a dokumentum formailag önálló része
- **az oldal jellemzőit** _–_ például margók, tájolás, élőfej, élőláb, oldalszámozás – szakaszonként külön-külön is beállíthatjuk
- **többhasábos** megoldással főleg újságokban találkozunk, ahol a szedéstükör olyan széles, hogy nehézkes a szemünkkel követni
- **Több szakaszra bontott dokumentum** esetén az élőfejet és az élőlábat beállíthatjuk szakaszonként, de lehetőségünk van arra is, hogy egy adott szakasz beállításai megegyezzenek az előzővel
## Számítógépes grafika és képszerkesztés
### **Pixelgrafika:**
> **Pixel vagy raszter-grafikus fájl:** egyes képpontok színkódjainak felsorolása
-   **1 képpont tárolása:** minden színre (red, blue, green) 8 bitnyi információval 256 különféle értéket vehet fel, így összesen 24 bit-en tárol 1 képpont információját

-   **Képnézegető (viewer) programok formátumai:**
	-   **JPG:** veszteség mentes képtömörítési eljárás, a legelterjedtebb formátum
	-   **PNG:** a PNG-hez hasonló veszteség mentes tömörítési eljárás, de JPG-vel ellentétben egy pixel információit nem 24, hanem 32 biten tárolja, mivel az RGB színkód mellett képes tárolni egyes képpontok átlászóságát is
	-   **GIF:** az egyik legrégebbi kepkiterjesztés, ami 256*256*256 színből egy 256 színből álló palettára képzi. Képes mozgóképek tárolására. A GIF ellenfele lehet az **APNG** ami túllép a GIF hiányosságain 
	-   **TIFF:** többrétegű képek leírására használt formátum. Elterjedtebb a használata a nyomdászatban és a GIS-rendszerekben (földrajzi információs rendszer)

- **Szerkesztő programok formátumai:**
	-   Ilyen formátumok tárolják az adott kép rétegeit, kijelöléseit, maskjait
	-   A GIMP formátuma az **XCF** a Photoshopé **PSD** vagy PSDX
	-   Ezek a fájlokat célszerű a saját szerkesztőprogramjukkal megnyitni

- **Fényképezőgép saját formátuma:**
	-   Ebbe a formátumba menti a fényképezőgép a fájlt exponáláskor
	-   Közös nevük a **RAW** (nyers)
	-   Rengeteg információt tartalmaznak, ami a képeken nem is látszódik pl.: kép világosításával láthatóvá válnak a képen addig egyöntetű sötét feketének tűnő területek részletei
	-   Ezek megnyitására általában általános célú megtekintő nem használható, hanem képszerkesztők
	-   Utólagos munkát Adobe Lightroommal vagy ennek ingyenes alternatívájával a Darktable-el lehet
	-   A lényegesen bonyolultabb utómunkára van szükség akkor használják az Adobe Photoshopot vagy ennek ingyenes alternatíváját a GIMPet 

- **Mire használják a pixelgrafikus szerkesztőprogramokat:**
-   A pixelgrafikus képek utólagos módosításához:
	-   Egyes részek átrajzolása
	-   Színek megváltoztatása
	-   Képrészletek cseréje
	-   Eltűntetés
	-   Az alkalmazás szűrőivel végzett módosítások
	-   Retusálás
-   Régen használták képregényfigurák, művészi grafikák és festmények ábrázolásához

### Vektorgrafika
> **vektorgrafika**: központi fogalma az alakzat, más néven geometriai elem. 
> Az alakzatok alaptulajdonságokkal rendelkeznek. Ilyen például a méret, a hely, a szín, a kitöltési tulajdonságok, az átlátszóság, a körvonal stb. A vektorgrafikai programok az ábrák elkészítését alakzatok létrehozásával, tulajdonságainak módosításával, célszerű átalakításával és együttes felhasználásával teszik lehetővé

- úgy nagyíthatjuk, hogy pixelesedés nem látható (fontos: térkép, a navigáció, a műszaki terv, egy logó)
- vektorgrafikai eszközök a legtöbb olyan szoftverben rendelkezésre állnak, ahol szükség van grafikai elemekre (pl word, powerpoint)
	- Irodai programok: *Microsoft Word és PowerPoint, LibreOffice Writer, Impress, Draw*
	-   Speciális célú programok: *GeoGebra, Euklides, Euler3D, Blender*
	-   Önálló vektorgrafikai szerkesztőprogramok: *Inkscape, CorelDraw, Adobe Illustrator*

SVG fájlok:
- kód első sora a használt XML verziószámát adja meg, amelyre a böngészőnek van szüksége
- tartalmát az `<svg>` jelölőben adjuk meg

> **Moaré:** óriásplakátokon, a digitális fényképeken, a vonalas és a szabályos mintájú ábrákon megjelenő nem várt mintázatok

## Bemutatókészítés
Az előadásunkat kísérő bemutatók készítésekor
-   használjunk minél nagyobb képeket;
-   ne írjuk ki azt, amit el is mondhatunk;
-   ha mégis írunk, akkor minél kevesebbet;
-   ha úgy érezzük, hogy egy dia zsúfolt, erősen fontoljuk meg a különálló diák használatát;
-   használjunk nagy és jól olvasható formájú betűket;
-   ne olvassuk fel azt, amit kiírtunk, mert zavaró;
-   legyünk szűkmarkúak az animációkkal;
-   legyen tervünk arra az esetre, ha a vetítésre használt gép nem jeleníti meg megfelelően a bemutatónkat

## Publikálás a világhálón
### HTML5 alapstruktúra
- első sor tartalmazza a **dokumentumtípust**: `<!DOCTYPE html>`
- következő sorba kerül a `<html>` tag, amely jelzi a böngészőnek, hogy egy HTML-dokumentumról van szó
	- `lang` paraméterben az oldal nyelvét kell megadnia – magyar nyelvű tartalom esetén a `hu` értéket, angol nyelvű tartalom esetén pedig az `en` értéket
- `<title>` tagben az oldal címét kell megadni
- `<body></body>` tagek közti rész a **dokumentumtörzs**
A teljes HTML-dokumentum `<html></html>` tartalma a **fejre** `<head></head>` és a **törzsre** `<body></body>` tagolódik
- bekezdések kialakításához a sorok elejére a `<p>`, a sorok végére a `</p>` taget kell elhelyezni
- hat címsorszintet használhatunk: 
	- legfelső (1-es szintű) címsor `<h1>`
	- alcímsorok `<h2>`, `<h3>`, ...
#### Szövegformázások
- félkövér: `<b>`
- dőlt: `<i>`
- olyan szövegeket emelhet ki, amelyen nagyon fontosak: `<strong>`
- hangsúlyos kiemelésre szolgál: `<em>`
- felsorolás: `<ul>` / számozás: `<ol>`
- listaelem: `<li>`
- sortörés: `<br>`
- kép beillesztés: `<img>`
- `<figure>` és `<figcaption>`
- hivatkozás: `<a>`
- `<video>` és `<source>`
- `<audio>` és `<source>`

Táblázat:
```html
<table>  
	<caption>cím</caption>  
	<tr>  
		<th>header row</th>
	</tr>  
	<tr>  
	    <td>data</td>
	</tr>
</table>
```

### CSS
- inline (elemközi stílus)
- külön css fájl
- beágyazott `<style>`
CSS-szabály két részből áll
- **kijelölő** / szelektor: segítségével kijelölheti azokat az elemeket, amelyeket formázni szeretne
- **deklarációs blokk**: kapcsos zárójelek között helyezkedik el, bennbe **deklarációk** 
	- **tulajdonságok**  és azok **értékei**

- színeket lehet rgb alapján, angol színnevekkel, HTML színkódokkal
- típus kijelölők, osztály kijelölők, azonosító kijelölő

Dobozmodell:
- width / height: tartalom szélessége / magassága
- padding: belső margó (tartalom és szegély között)
- margin: szegély és a többi elem közötti térköz

## Táblázatkezelés 
#### Cellák tartalma
- **szám**: 
	- **számformátum**: tizedesjegyeinek száma változtatható a megjelenítésben
	- **százalékformátum**: a szám százszorosát jeleníti meg, és azt a százalék (%) jellel egészíti ki
	- **dátum- és időformátum**: a szám egészrészét dátumként, a törtrészét pedig időként jeleníti meg (1900. január 1 a kezdő)
	- **pénznemformátum**: a számot kiegészíti a pénznem jelével, amely a mértékegységhez hasonlóan jelenik meg
	- **egyéni formátum**
- **szöveg**
- **logikai érték** (IGAZ / HAMIS)
#### Cellahivatkozások
> **Relatív cellahivatkozás:** A kifejezés másolásakor a másolás irányának megfelelően módosul
> **Abszolút cellahivatkozás**: A kifejezés másolásakor a cellahivatkozás nem változik, a táblázatkezelő program a cella tényleges helyét tárolja
> **Vegyes** **cellahivatkozás:** A kifejezés másolásakor a cellahivatkozásban az egyik koordináta abszolút, a másik relatív. A koordináta rögzítésétől függően vagy a vízszintes, vagy a függőleges irányú elmozdulásnak megfelelően változik a hivatkozás.

### Függvények
- újraszámítást magunk is kezdeményezhetjük az F9 gomb megnyomásával
- függvények beszúrását függvényszerkesztő funkció segítifüggvények beszúrását függvényszerkesztő funkció segíti
- kategóriák:
	- statisztikai
	- matematikai / trigonometriai
	- dátum és idő
	- logikai
	- keresési és hivatkozási
	- szöveg
	- adatbázis
- `...HATÖBB()` függvények esetén a kritériumok között mindig **ÉS** kapcsolat van

## Adatbázis-kezelés