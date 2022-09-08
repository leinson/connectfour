## Määrittelydokumentti

### Aihe
Connect Four-peli.

Ohjelmointi- ja dokumentaatiokielet:
Python ja suomenkieli.

### Algoritmit ja tietorakenteet
Mitä algoritmeja ja tietorakenteita toteutat työssäsi?
Mitä ongelmaa ratkaiset ja miksi valitsit kyseiset algoritmit/tietorakenteet?
Tavoitteena olevat aika- ja tilavaativuudet (m.m. O-analyysit)

Projektissani hyödynnän *minimax-algoritmia*, jota yritän tehostaa *alpha-beta karsinnalla*.

Valitsin nämä algoritmit, koska kirjallisuuden perusteella nämä toimivat hyvin kahden hengen vuoropeleissä,
kuten valitsemassani Connect Four pelissä. 
Pelin voisi kehittää niin, että tietokone satunnaisesti valitsee siirtojensa paikat. Ongelmaksi tällöin
muodostuu se, että tietokonevastustajan päihittäminen on turhan helppoa.
Tässä työssä haluan kehittää tietokonevastustajan, joka mahdollisimman hyvin saisi valittua 
siirtonsa niin, että peli on ihmiselle haastava pelata.
Yllä mainittuja algoritmeja käyttämällä voin ratkaista kyseisen ongelman luomalla tekoälyn, 
jonka siirrot eivät ole satunnaisia vaan järkeviä, ja tuottavat haasteellisen pelin.


Tavoitteellisten aika- ja tilavaativuuksien pohdintaan hyödynsin Wikipedian Alpha-beta pruning - sivustoa. 
Alpha-beta karsinta yrittää vähentää läpikäytävien haarojen määrää, mitä minimax automaattisesti kävisi läpi.
Pahimmassa tapauksessa voi käydä niin, että aikavaativuus on täysin sama kuin minimaxin eli O( $b^d$ ) 
alpha-beta karsinnan jälkeen, kun b=branching factor ja d=haun syvyys d vuorojen verran. 
Jos pystymme optimoimaan haarojen läpikäymisen järjestystä niin, että ensin käydään läpi parhaimmat mahdolliset haarat,
voi aikavaativuus pudota jolloin on mahdollista saada O( $\sqrt{b^d}$ ). 

tietorakenteet? 




### Ohjelman syötteet
Mitä syötteitä ohjelma saa ja miten näitä käytetään?
Käytetään graafisen käyttöliittymän avulla: käyttäjä valitsee sarakkeen, johon pudottaa kiekkonsa.



### Lähteet
https://tiralabra.github.io/2022_p1/fi/aiheet/
https://en.wikipedia.org/wiki/Minimax
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
