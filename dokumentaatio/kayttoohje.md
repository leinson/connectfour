## Käyttöohje

### Ohjelman käynnistäminen

- Lataa ohjelma esimerkiksi zip-pakettina omalle koneellesi.
- Riippuvuudet asennetaan ennen sovelluksen käynnistämistä komennolla: `poetry install`
- Sovelluksen käynnistäminen tehdään komennolla: `poetry run invoke start`

### ConnectFour pelaaminen

- Peli noudattaa Connect Four- pelin perinteisiä sääntöjä. Voittoon vaaditaan 4 omaa nappulaa vierekkäin. Tämän voi tehdä pysty-, vaaka-, tai diagonaalisuunnassa.
- Graafisessa käyttöliittymässä pääset heti pelinäkymään. Valitset hiiren painalluksella, mihin sarakkeeseen haluat pudottaa nappulasi. Tämän jälkeen tekoäly tekee oman siirronsa, jonka jälkeen on jälleen sinun vuorosi. 
- Peli jatkuu, kunnes lauta on täynnä tai jompikumpi voittaa.

### Sovelluksesta poistuminen

- Kun olet valmis, poistu sovelluksesta sulkemalla ikkuna.

### Testien ajaminen

- Testit ajetaan `poetry run invoke test`
- Testikattavuusraportti ajetaan `poetry run invoke coverage-report`, jolloin raportti löytyy htmlcov kansiosta tiedostosta index.html (avaa selainnäkymään).
