## Määrittelydokumentti

### Aihe
Connect Four-peli.

### Ohjelmointi- ja dokumentaatiokielet:
Python ja suomenkieli.

### Algoritmit ja tietorakenteet

Projektissani hyödynnän *minimax-algoritmia*, jota yritän tehostaa *alpha-beta karsinnalla*. 


Valitsin nämä algoritmit, koska kirjallisuuden perusteella nämä toimivat hyvin kahden hengen vuoropeleissä,
kuten valitsemassani Connect Four pelissä. 
Pelin voisi kehittää niin, että tietokone satunnaisesti valitsee siirtojensa paikat. Ongelmaksi tällöin
muodostuu se, että tietokonevastustajan päihittäminen on turhan helppoa.
Tässä työssä haluan kehittää tietokonevastustajan, joka mahdollisimman hyvin saisi valittua 
siirtonsa niin, että peli on ihmiselle haastava pelata.
Yllä mainittuja algoritmeja käyttämällä voin ratkaista kyseisen ongelman luomalla tekoälyn, 
jonka siirrot eivät ole satunnaisia vaan järkeviä, ja tuottavat haasteellisen pelin.

Minimaxissa luodaan pelipuu, jossa juurisolmu on aloitustilanne ja tämän lapsisolmut ne tilanteet, kun yksi siirto on tehty. Sama rakenne toistuu näille lapsisolmuille, ja niin edelleen rekursiivisesti, kunnes toivottu määrä tasoja on rakennettu. Tämän jälkeen algoritmi käy solmut läpi rekursiivisesti syvyyshaun lailla. Alimpien lehtisolmujen arvoja verrataan toisiinsa, ja riippuen kumman vuoron taso on kyseessä valitaan joko minimi tai maksimi arvo. Lopuksi juurisolmuun on päivitetty arvo joka on paras mahdollinen tulos, jos molemmat pelaajat tekevät parhaimmat siirrot, jonka perusteella tekoäly voi tehdä valintansa. Algoritmi toistetaan joka kerta, kun vastustaja eli ihminen on tehnyt siirtonsa.

Alpha-beta-karsinnan avulla pääsemme eroon turhien solmujen läpikäynnistä ja näin saadaan tehokkaampi ja nopeampi algoritmi aikaiseksi. Algoritmi huomioi minimi ja maksimiarvojen lisäksi alpha ja beta arvot, joita käytetään karsimaan ne haarat tai solmut, joita ylempi taso ei ikinä valitsisi. 

Tavoitteellisten aika- ja tilavaativuuksien pohdintaan hyödynsin Wikipedian Alpha-beta pruning - sivustoa. 
Alpha-beta karsinta yrittää vähentää läpikäytävien haarojen määrää, mitä minimax automaattisesti kävisi läpi.
Pahimmassa tapauksessa voi käydä niin, että aikavaativuus on täysin sama kuin minimaxin eli O( $b^d$ ) 
alpha-beta karsinnan jälkeen, kun b= haarautuminen (branching factor) ja d=haun syvyys d vuorojen verran. 
Jos pystymme optimoimaan haarojen läpikäymisen järjestystä niin, että ensin käydään läpi parhaimmat mahdolliset haarat, voi aikavaativuus pudota jolloin on mahdollista saada O( $\sqrt{b^d}$ ). Tilavaativuudesta en hirveästi lähteitä löytänyt. Kyseessä on kuitenkin rekursiivinen algoritmi, joka ei vaadi staattista tietorakennetta vaan varaa dynaamisesti muistista tilaa sen edetessä, ja vapauttaa tilaa purkautuessa. Kunhan pelipuun tasojen määrä pidetään maltillisena, ei tilavaativuuden pitäisi aiheuttaa ongelmaa. 



### Ohjelman syötteet
Ohjelmaa käytetään graafisen käyttöliittymän avulla. Ajatus on, että käyttäjä valitsee sarakkeen, johon pudottaa kiekkonsa, joko hiirellä tai näppäimistöä käyttämällä. Muita syötteitä ei luultavasti ohjelman toiminnallisuuden kannalta tarvita.


### Lähteet
https://tiralabra.github.io/2022_p1/fi/aiheet/

https://en.wikipedia.org/wiki/Minimax

https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

https://jyx.jyu.fi/bitstream/handle/123456789/58204/1/URN%3ANBN%3Afi%3Ajyu-201805292875.pdf



Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti (TKT)
