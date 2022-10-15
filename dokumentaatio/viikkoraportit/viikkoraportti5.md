## Viikkoraportti 5

**Tuntikirjanpito: 14h**

Tällä viikolla olen saanut erityisesti minimaxia ja ohjelman toimivuutta edistettyä. 
Implementoin alpha-beta karsinnan algoritmiin, jonka myötä sain ohjelman pyörimään suuremmalla syvyydellä.
Tein yksinkertaisen heurestiikalaskennan, joka tarkistaa, onko voitto jommallakummalla pelaajista. Tämä vaikuttaa jo itsessään antavan AI:lle todella
hyvät eväät paremmalle suoritukselle.
Hyödynsin myös neuvoa järjestyksestä, missä kannattaa käydä sarakkeet läpi. Tämä auttoi nopeudessa sekä myös johti parempiin AI:n valintoihin. 
Ohjausajalla sain hyviä vinkkejä, miten ohjelmaa voisi vielä tehostaa. Näistä ehdin muutamia alkaa kokeilemaan. 
Poistin turhan heurestiikkafunktiokutsun, jos voitto oli jo todettu. 

Sain myös vihdoin minimaxin toimimaan graafisessa käyttöliittymässä. Nyt ohjelman testaus on helpompaa ja selkeempää.
Korjasin myös graafisen käyttöliittymän indeksointivirheitä, jos klikkaa hieman sarakkeen ohi.

Refaktoroin myös ohjelmaani siten, että siirsin minimaxin omaan tiedostoonsa. Tämä selkeytti mielestäni ohjelman rakennetta.
Jos jää aikaa, teen ehkä muutamia muita hienosäätöjä - voisin muutamaa isoa funktiota jakaa pienempiin. 

Mikään ei tällä hetkellä ole varsinaisesti epäselvää, täytyy vain työstää eteenpäin. Olen tyytyväinen, että olen saanut projektini tässä vaiheessa
tähän vaiheeseen, koska viimeisillä viikoilla minulla on vähemmän aikaa työstää tätä.

Seuraavalla viikolla aloitan minimax funktion testauksen, yritän optimoida minimaxia vielä tehokkaammaksi, vaihdan tasapeli-tarkistuksen fiksummaksi.
Ehkä parannan vielä heurestiikkaani, voisin yrittää lisätä 3 rivissä - pisteytyksen myös. 
Työstän dokumentteja eteenpäin. Näiden jälkeen hion vielä hieman graafista käyttöliittymää.


