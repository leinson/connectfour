## Viikkoraportti 6

*Tuntikirjanpito:* 15h

Tällä viikolla olen hienosäätänyt ohjelman rakennetta, tehnyt refaktorointia ja yrittänyt karsia pois ylimääräisiä funktiokutsuja. Esimerkiksi get_possible_columnsia kutsuin useaan otteeseen, vaikka olisin voinut hyödyntää aiemmin saatua tulosta. Muutin myös hieman järjestyksiä, missä mitäkin asiaa tarkistetaan ja kutsutaan, jotta ohjelma ei turhaan hae etukäteen jotain tietoa, jos se on esimerkiksi poistumassa funktiosta heti sen jälkeen. 

Olen saanut testauksen lähes valmiiksi. Tein minimax-funktioon liittyviä yksikkötestejä "valitseeko tekoäly oikean sarakkeen pelitilanteen perusteella"-tyyppisesti, ja niiden mukaan tekoäly toimii niinkuin pitääkin. Testausdokumenttia kirjoitettu.

Olen työstänyt graafista käyttöliittymää mieluisaksi. Nyt ohjelman tulosteet näkyvät itse ohjelmassa eikä terminaalissa. Poistin gitistä komentorivikäyttöliittymän. koska graafisessa versiossa on nyt kaikki tarvittavat ominaisuudet. 

Pohdin myös minimax algoritmin tehostamista. Lisäsin tarkistuksen, jonka pitäisi priorisoida matalan tason syvyyden voittoja. Siistin minimaxia niin, että terminal nodeen liittyvät tarkistukset tapahtuvat kyseisessä funktiossa eikä minimaxissa. 
Päätin kuitenkin tietoisesti jättää muut tehostamiseen liittyvät muutokset pois (minimaxin katkaiseminen, jos syvyyden kesto on yli tietyn rajan/heurestiikan parantaminen). Mielestäni sovellus toimii riittävän hyvin ja olen siitä erittäin tyytyväinen. Lisäksi minun täytyy priorisoida myös muiden kurssien tenttejä/projekteja. Halusin myös käyttää aikani siihen, että saan testauksen mahdollisimman kattavaksi ja että se koodi mikä minulla nyt on tuotettuna on mahdollisimman siisti.

Lisäksi tietenkin toisen vertaisarvioinnin tekemistä. Tämä olikin haastavampi arvioida kuin ensimmäinen, koska tässä oli käytetty runsaasti HTML:ää sekä paljon kirjastoja jotka eivät olleet itselleni entuudestaan tuttuja. 

Viimeisillä viikoilla tulen kirjoittamaan dokumentointiin liittyvät tiedostot valmiiksi sekä tehdä final checkit koodini suhteen että kaikki on kunnossa. 