### Viikkoraportti 2


**Tuntikirjanpito vko 2 : ~13h**

Tällä viikolla olen lisännyt muut tarvittavat riippuvuudet projektilleni. Olen lisännyt pylintin koodin laaduntarkastamista varten,
autopep8 automaattiseen formaattikorjauksen avuksi ja invoken helpottamaan tehtävien suorittamista. Olen aloittanut (yksikkö)testien tekemisen pytestillä
projektin koodin rinnalla ja käyttänyt coverage työkalua testikattavuusraporttien tekemistä varten. Viimeisin raportti löytyy tästä
dokumentaatiokansiosta testikattavuus kansion sisältä. Testaukset olen rajoittanut nyt functions.py tiedostoon, sillä index.py toimii tällä 
hetkellä käyttöliittymänä, ja ainakin ohte-kurssilla ohjeistettiin jättämään käyttöliittymä testauksen ulkopuolelle.

Ohjelmani on päässyt alkuun, ja olen yrittänyt saada toteutettua tärkeimpiä toimintoja ennen kun hyppään pygamen ja tekoälyalgoritmin maailmaan.
Ohjelma toimii tällä hetkellä komentorivillä, ja siinä pystyy pelaamaan tietokonetta vastaan joka valitsee satunnaisesti oman sarakkeen.
Voittotarkistus toimii tällä hetkellä vain sarakkeiden suhteen. Olen hyödyntänyt docstringiä koodin kommentoimista varten.

Vaikka onkin vielä hyvin alkeellinen, olen silti aika tyytyväinen siihen mitä olen
saanut aikaiseksi, koska alkuun tuntui erittäin kankealta ja hankalalta edes tietää mistä aloittaa. Opin paremmin käsittelemään taulukkoja,
jota käytän pelilaudan pohjana. Matriksien käsittelyt ovat aina tuntuneet itselleni jotenkin hankalilta.
En ollut aiemmin käytättnyt numpy kirjastoa sen enempää, joten pääsin hieman tutustumaan siihen. Huomasin testejä
tehdessä, että numpy taulukkoja ei voi perinteisesti verrata toisiinsa koska ovat olioita, joten pääsin siinä käyttämään numpyn testing moduulia. 

Seuraavaksi täytyy saada voitontarkistukset rivi- ja horisontaalisesti toimimaan. Aloitan varmaan pygamen käyttöönoton, joka vaatii hieman 
harjoittelua, käyttänyt viimeksi ohjan loppuprojektissa. Seuraavaksi onkin eri virhesyötteiden tms eliminointi ja itse "tekoäly-algoritmin" työstäminen, 
ja siihenhän sitten sitä aikaa pääseekin kivasti kulumaan. :-)

### Vaikeudet/epäselvyydet/kysymykset

Kurssin introluennolla oli puhetta, että tällä kurssilla ei ole tärkeää seurata täysin olio-ohjelmointiparadigmaa, koska se voi jopa tietyissä
tilanteissa hidastaa ohjelman suoritusta. Lähdin nyt itse tuota projektia tekemään funktio- ja metodikutsuihin pohjautuen, koska se tuntui tässä 
luonnolliselta. 
Koodia ei ole vielä hirveitä määriä, joten periaatteessa voisin vielä muuttaa sitä enemmän olio-ohjelmoinnin suuntaan, mutta onko siinä järkeä? 
Tuleeko "miinuspisteitä" jos ohjelman koodi on tällä tavalla metodeja ja funktioita kutsuen toteutettu eikä oliopohjainen?


