# Testausdokumentti

Ohjelmaa on testattu sekä manuaalisesti että automatisoiduilla yksikkötesteillä läpi kehityksen.

## Yksikkötestaus

### Sovelluslogiikan testaus

Ohjelmassa on testattu sovelluslogiikasta vastaavaa koodia. Sovelluslogiikasta vastaavat tiedostot ovat functions ja minimax_a_b. Näiden tiedostojen metodit ovat jaettu eri testiluokkiin tiedostoihin **functions_test.py**: TestFunctions ja TestCheckIfWin, ja **minimax_a_b_test.py**: TestMiniMax ja TestMiniMaxHelpFunctions.

Testit ajetaan komennolla `poetry run invoke test`. Tämä komento suorittaa kaikki yksikkötestit, ja tuloste muodostuu terminaaliin onnistuneista (tai epäonnistuneista) testeistä. 

Yksikkötestit ovat tehty Unittest-työkalulla. Tämän avulla on luotu testejä, jotka testaavat tiettyä toiminnallisuutta, tietystä funktiosta, tietyllä syötteellä. Testejä on pyritty tekemään mahdollisimman kattavasti, lisätietoa testikattavuudesta alla. Jokaiselle funktiolle on tehty jokin testi, ja usealle funktioille on tehty monia testejä. Useat testit samasta funktiosta ovat tarpeellisia, kun esimerkiksi saatu syöte muuttaa funktion toimintaa vaikka ehtolausekkeiden kautta. Monia testejä luodessa on testattu myös virheellistä vertailua varmistamaan, että läpi mennyt testi oikeasti tarkoittaa, että testattu toiminnallisuus toimii oikein. 

Testeissä ei olla testattu jokaista erilaista tapaa saada voittoa, koska tämä veisi runsaasti aikaa. Sen sijaan on yritetty monipuolistaa eri testien lautasyötteitä, varioiden riviä ja sarakkeita, missä voitto on. Esimerkiksi kaikki voittotestit eivät ala ruudusta (0,0). Syötteet, joilla testejä on suoritettu, näkyvät yksikkötesteissä.

Testien suorittaminen vie noin 4,5 sekuntia. 

### Testikattavuus

Testikattavuuden laskemiseen on käytetty Coverage työkalua, joka luo yksikkötestien pohjalta testikattavuusraportin html-tiedostoon. 
Testikattavuuden saa suoritettua testien suorittamisen jälkeen komennolla `poetry run coverage-report`. 
Testauksen haarautumakattavuus on tällä hetkellä 98%. Testikattavuus lasketaan functions.py ja minimax_a_b.py tiedostoista. 

![](./testikattavuus/coveragereport15oct.png)

Yllä kuva ajankohtaisesta testikattavuudesta. Viikkottaiset testikattavuusraportit sijaitsevat dokumentaatio-kansion alakansiossa testikattavuus.

Käyttöliittymä on ohjeiden mukaisesti jätetty testikattavuuden ulkopuolelle.

#### Suorituskykytestaus
Varsinaista suorituskykytestausta ei ole erikseen toteutettu. Havainnointia on kuitenkin tehty manuaalisesti testejä ja ohjelmaa suorittaessa, minkä verran tekoälyn siirto kestää. Tämän vuoksi syvyys 6 valikoitui, koska kertaakaan ei tullut tilannetta, missä tekoäly olisi laskelmoinut seuraavaa siirtoaan enemmän kuin 10 sek. Tämän ajan käyttäjä jaksaa todennäköisesti odottaa tekoälyn siirtoa.

### Asennus
Sovellusta on testattu Linux-ympäristössä, missä sovellus on kehitetty. Täten sovellus on todettu toimivaksi Linuxissa. Muissa ympäristöissä sovellusta ei ole testattu.

## Manuaalinen testaus
Ohjelmaa on testattu runsaasti manuaalisesti läpi ohjelman kehityksen. Print tulostuksia terminaaliin on ollut käytössä lähes jokaisessa funktiossa jossain vaiheessa kehityksen aikana. Minimax-funktion rekursiota on mm. tällä tavalla seurattu, ja tulosteissa päästy näkemään miten funktio poimii heurestiikasta annettuja arvoja.

Peliä on myös pelattu testimielessä alusta lähtien. Peliä on yritetty pelata mahdollisimman monipuolisesti, antaen tekoälyn voittaa tyhmillä siirroilla, ja yrittäen parhaimmalla tavalla voittaa tekoälyn. Samalla on havainnoitu tapaa, miten tekoäly valitsee siirtojaan ja verrattu niitä print tulosteisiin heurestiikan tuloksista - valitseeko tekoäly varmasti parhaimman mahdollisen sijainnin sen perusteella, mitä tietoja sillä on. 

## Toiminnallisuudet ja sovellukseen jääneet laatuongelmat 

Testejä voisi vielä laajentaa kattamaan runsaampia määriä esimerkillisiä lauta-tilanteita varmistamaan, että ohjelma varmasti toimii oikein erilaisissa tilanteissa. Katso ystävällisesti toteutusdokumentti muiden ongelmien / parannuksien suhteen. 
