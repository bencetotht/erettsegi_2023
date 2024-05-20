# SQL
## Joinok
|MŰVELET|HASZNÁLAT|
|:-:|:-:|
|`INNER JOIN`|metszet|
|`LEFT JOIN`|bal oldali táblába lévőket|
|`RIGHT JOIN`|jobb oldali táblába lévőket|
## Műveletek
|MŰVELET|HASZNÁLAT|
|:-:|:-:|
|`INSERT INTO táblanév(mezőnevek) VALUES(értékek)`| beillesztés|
|`UPDATE táblanév SET mezőnév=érték, … WHERE feltétel`|frissítés|
|`DELETE FROM táblanév WHERE feltétel`|törlés táblából|
|`CREATE TABLE táblanév AS SELECT * ...`|adattábla lekérdezés eredményéből |
|`ALTER TABLE táblanév ADD COLUMN nev INT`|tábla bővítése újabb mezővel|
|`DROP TABLE táblanév`|tábla törlése|
|`TRUNCATE táblanév`| tábla ürítése|
Random szám: `FLOOR(RAND()*range + 1)`
## Halmazműveletek
|MŰVELET|HASZNÁLAT|
|:-:|:-:|
|`UNION`|két lekérdezés eredményének egyesítése|
|`INTERSECT`|két lekérdezés közös része|
|`EXCEPT`|első lekérdezésből vonjuk ki a második lekérdezést|
## Függvények
|FÜGGVÉNYCSOPORT|FÜGGVÉNYEK|
|:-:|:-:|
|Aggregáló|`MIN()`, `MAX()`, `COUNT()`, `SUM()`, `AVG()`|
|Egyszerű idő|`YEAR()`, `MONTH()`, `DAY()`, `HOUR()`, `MINUTE()`, `SECOND()`|
|Idő különbség|`TIMEDIFF(IDŐÉRTÉK1, IDŐÉRTÉK2)`, `DATEDIFF(IDŐÉRTÉK1, IDŐÉRTÉK2)`
|Current|`CURDATE()`, `CURTIME()`| 
|Idő módosítás|`ADDTIME("06:30:00", "00:45:00")` / `SUBTIME(IDŐÉRTÉK1, IDŐÉRTÉK2)`, `ADDDATE("2022-02-01", 4)` / `SUBDATE(DÁTUM, ÉRTÉK)`|
| megmondó faszom |`WEEKDAY(DÁTUM)`, `DAYNAME(DÁTUM)`, `MONTHNAME(DÁTUM)`|
|Szövegek|`FORMAT(SZÁMÉRTÉK, PONTOSSÁG)`,`CONCAT()`,`LOCATE()`,`LOWER()`,`UPPER()`,`SUBSTRING(SZÖVEG, POZÍCIÓ, HOSSZ)`,`LEFT()`,`RIGHT()`|
|Egyéb|`RAND()`, `FLOOR()`, `MOD(A, B)`, `DIV(A, B)`, `CEIL()`, `ROUND()`, `IF(feltétel, ha igaz, ha hamis)`, `ABS()`, `IFNULL(param1, param2)`|

# Python
## Text formatting
|function|usage|
|:-:|:-:|
|.replace("egy", "KÉT")||
|.find("gy")+1||
|.capitalize()||
|.strip()||
|.lstrip()||
|.rstrip()||
## Halmazok
|function|usage|
|:-:|:-:|
|.add('elem')||
|.discard('elem')|continue|
|.remove('elem')|crash|
|.pop('elem')||
|.clear()||
![[Pasted image 20230509151058.png]]
## Szótárak
|function|usage|
|:-:|:-:|
| szótár['kulcs'] = 'érték'||
|if 'kulcs' in szótár.keys()||
|if 'érték' in szótár.values()||
|del szótár['kulcs']||
|szótár.pop('kulcs')||
## Rendezés
```python
sorted(data_2011, key=lambda x: x['num'], reverse=True)
```

# Excel
|FÜGGVÉNYCSOPORT|FÜGGVÉNYEK|
|:-:|:-:|
|Statisztikai|=ÁTLAG(), =DARAB(), =DARAB2(), =DARABTELI(), =MAX(), =MIN(), =NAGY(), =KICSI(), =DARABÜRES(), =DARABTÖBB(), =ÁTLAGTÖBB(), =MAXHA(), =MINHA()
|Matematikai és trigonometriai|=ABS(), =GYÖK(), =KEREKÍTÉS(), =KEREK.LE(), =KEREK.FEL, =MARADÉK(), =HATVÁNY(), =PI(), =SZUM(), =SZUMHA(), =SZUMHATÖBB(), =VÉL(), =VÉLETLEN.KÖZÖTT()
|Dátum és idő|=ÉV(), =HÓNAP(), =NAP(), =ÓRA(), =PERCEK(), =MPERC(), =DÁTUM(), =IDŐ(), =HÉT.NAPJA(), =MA(), =MOST()
|Logikai|=ha(), =és(), =vagy(), =nem()
|Keresési és hivatkozás|=FKERES(), =VKERES(), =INDEX(), =HOL.VAN(), =XKERES()
|Szöveg|=BAL(), =JOBB(), =KÖZÉP(), =HOSSZ(), =KISBETŰ(), =NAGYBETŰS(), =SZÖVEG.KERES(), =SZÖVEG.TALÁL(), =ÖSSZEFŰZ(), =HELYETTE(), =ÉRTÉK()
|Adatbázis|=AB.SZUM(), =AB.ÁTLAG(), =AB.DARAB(), =AB.DARAB2(), =AB.MIN(), =AB.MAX(), =AB.MEZŐ()
|Sorba rendezés|=Rang.Eq(szám;hiv)|
|Szöveg átalakítás|=SZÖVEG(A2;"nnnn")|

# CSS
![[Pasted image 20230511115834.png]]