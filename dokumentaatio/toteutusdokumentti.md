## Toteutusdokumentti

kesken.

### Ohjelman yleisrakenne

Ohjelma koostuu tällä hetkellä kahdesta kokonaisuudesta: käyttöliittymä ja sovelluslogiikka. Käyttöliittymä on toteutettu Pygamella tiedostossa ui.py. Sovelluslogiikka on toteutettu tiedostoon functions.py ja minimax.py. Functions.py kutsutaan käyttöliittymästä, ja minimax.py funktioita kutsutaan functions.py funktioista. Nämä molemmat sisältää funktioita ja metodeja joita kutsutaan käyttöliittymän kautta tai niiden sisältä. 

Ohjelmassa käyttäjä pelaa tietokoneen tekoälyä vastaan. Käyttäjä valitsee sarakkeen, johon pudottaa oman nappulansa. Tekoäly hyödyntää minimax algoritmia valitsemaan oman siirtonsa. Ohjelma tarkistaa jokaisen syötön jälkeen, onko voittoa havaittavissa. Jos on voitto, peli päättyy. 

### Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)
Suorituskyky- ja O-analyysivertailu (mikäli työ vertailupainotteinen)

Aikavaativuus mitä yritin tavoittella, oli .... Saavutin oman arvioni mukaan .... 
Tilavaativuudeesta: kyseessä on rekursiivinen algoritmi, joka ei vaadi varsinaisesti staattista isoa tietorakennetta vaan varaa dynaamisesti muistista tilaa sen edetessä, ja vapauttaa tilaa purkautuessa. Alfa-beta karsinnan myötä rekursion suuruuttakin saadaan rajoitettua. Varsinaista tilavaativuutta en pseudokoodeista algoritmille löytänyt.

### Työn mahdolliset puutteet ja parannusehdotukset

- Minimax algoritmia voisi vielä tehostaa paremmalla heurestiikalla. Lisäksi voisi rajata haun syvyyttä ottamalla huomioon yhden kerroksen keston, ja katkaisemalla minimax sen jälkeen, kun yhden kerroksen suorittaminen kestää esimerkiksi yli 10sek.
- Käyttöliittymää voisi parantaa antamalla käyttäjälle mahdollisuus valita vaikeustason ja pelin uudelleenkäynnistämisen ohjelman sisällä.


### Lähteet
https://tiralabra.github.io/2022_p1/fi/aiheet/

https://en.wikipedia.org/wiki/Minimax

https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

https://jyx.jyu.fi/bitstream/handle/123456789/58204/1/URN%3ANBN%3Afi%3Ajyu-201805292875.pdf

https://www.youtube.com/watch?v=y7AKtWGOPAE&t=0s

https://dr0id.bitbucket.io/legacy/pygame_tutorial00.html

https://pygame.readthedocs.io/en/latest/1_intro/intro.html
