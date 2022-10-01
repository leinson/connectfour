## Viikkoraportti 4

**Tuntikirjanpito: 15h**

Tällä viikolla olen saanut aloitettua minimax-algoritmin toteutusta ja siihen liittyviä muita metodeja. Tämä on tällä hetkellä yhdistetty komentorivin käyttöliittymään. Tähän onkin kulunut runsaasti aikaa. Kertasin minimaxin toimintaa lähteistä ja youtube videoista. Nyt tuntuu siltä, että oikeasti ymmärrän miten se toimii, ja sainkin itse minimaxin rungon eli rekursion toimimaan jokseenkin oikealla tavalla. En kuitenkaan ollut tajunnut, miten isossa osassa heurestiikka ja siirtojen pisteiden laskenta on itse algoritmin toimivuudessa. Ihmettelinkin, mistä kaikkien minimax-esimerkkien terminal-nodejen numerot tulevat.. Sehän sitten selvisi yhdestä youtube videosta, että se logiikka täytyy itse rakentaa. Samaisesta videosta sain hieman vinkkejä siihen, miten asiaa kannattaa lähestyä. Pisteytys on itselläni vielä todella kesken, jonka vuoksi en toisaalta osaa sanoa, toimiiko vielä minimax-algoritmin muut komponentit kokonaisuudessaan oikein, koska tekoälyn valinnat eivät ole vielä älykkäitä.

Olen myös lisännyt yksikkötestien määrää, mutta en ole kaikkiin uusiin minimaxiin liittyviin komponentteihin ehtinyt testejä kirjoittaa.

Seuraavaksi jatkan minimaxin hiomista, testausta ja heurestiikan/pisteytyksen tekemistä. Kun näen, että ne toimivat, lisään alpha-beta-karsinnan. Sitten täytyy vielä käsitellä virhesyötöt, yhdistää minimax graafiseen käyttöliittymään ja parantaa ulkoasua (jos aika riittää). Näiden lisäksi toki vielä testaus- ja toteutusdokumenttien täydentäminen. 

### Epäselvyydet:
Minkälaista testausta tällaiseen tekoäly-peliin tarvitsee noiden yksikkötestien lisäksi? Tarkoittaako suorituskykytestaus ohjelman nopeuden tarkistamista - ja toteutetaanko tämä ottamalla aikaa, miten kauan esim yksi tekoälyn siirto kestää? Ohte-kurssilla käytiin vain noita unittestejä läpi.