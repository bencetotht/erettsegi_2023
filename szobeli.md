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
## Adatbázis-kezelés