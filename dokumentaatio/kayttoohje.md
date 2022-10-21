## Käyttöohje

### Ohjelman käynnistäminen

- Lataa ohjelma haluamallasi tavalla (esimerkiksi zip-pakettina) omalle koneellesi
- Asenna tarvittaessa poetry
- Riippuvuudet asennetaan ennen sovelluksen käynnistämistä komennolla: `poetry install` projektin juurikansiossa
- Siirry poetryn virtuaaliympäristöön komennolla: `poetry shell`
- Sovelluksen käynnistäminen tehdään komennolla: `poetry run invoke start`, joka ajaa index.py tiedoston.

### ConnectFour pelaaminen

- Peli noudattaa Connect Four- pelin perinteisiä sääntöjä. Voittoon vaaditaan 4 omaa nappulaa vierekkäin. Tämän voi tehdä pysty-, vaaka-, tai diagonaalisuunnassa.
- Pääset heti pelinäkymään. Valitse hiiren painalluksella, mihin sarakkeeseen haluat pudottaa nappulasi. Tämän jälkeen tekoäly tekee oman siirronsa, jonka jälkeen on jälleen sinun vuorosi etc. 
- Peli jatkuu, kunnes lauta on täynnä, tai jompikumpi voittaa.

### Sovelluksesta poistuminen

- Kun olet valmis, poistu sovelluksesta sulkemalla ikkuna.

### Testien ajaminen

- Testit ajetaan komennolla: `poetry run invoke test`
- Testikattavuusraportti ajetaan komennolla: `poetry run invoke coverage-report`, jolloin raportti löytyy htmlcov kansiosta tiedostosta index.html (avaa selainnäkymään).
