# Testausdokumentti
Ohjelmaa on testattu sekä manuaalisesti automatisoiduilla yksikkö- ja integraatiotesteillä läpi kehityksen.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka
Sovelluslogiikasta vastaava luokka on tällä hetkellä Functions, ja sillä on oma testiluokka TestFunctions.

### Testauskattavuus
Testauksen haarautumakattavuus on tällä hetkellä 64%. 

![](./testikattavuus/coverage_report_24_sept.png)

Näet viikkottaiset testikattavuusraportit dokumentaatio-kansion alakansiosta testikattavuus.

Käyttöliittymä on jätetty testikattavuuden ulkopuolelle. Käyttöliittymiä on tällä hetkellä kaksi: index.py toimii komentorivillä, ja ui.py pygamella graafisesti.

### Järjestelmätestaus
Järjestelmätestausta on suoritettu manuaalisesti. 

### Asennus
Sovellusta on testattu Linux-ympäristössä, missä sovellus on kehitetty.

### Toiminnallisuudet ja sovellukseen jääneet laatuongelmat 
Testausta on aloitettu, mutta testit eivät vielä kata koko ohjelmaa. Virhesyötöillä saa vielä sovelluksen kaatumaan. 
Kyseisiä asioita täydennetään sovelluksen kehityskaaren aikana. 
 
