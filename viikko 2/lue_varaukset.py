"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    varaus = varaus.split('|')

    varausnumero = int (varaus[0])
    varaaja = varaus[1]
    from datetime import datetime
    paiva = datetime.strptime(varaus[2], "%Y-%m-%d").date()
    suomalainenPaiva = paiva.strftime("%d.%m.%Y")
    aika = datetime.strptime(varaus[3], "%H:%M").time()
    suomalainenAika = aika.strftime("%H.%M")
    tuntimaara = int(varaus[4])
    tuntihinta = float(varaus[5])
    kokonaishinta = tuntimaara * tuntihinta
    maksettu = bool(varaus[6])
    kohde = varaus[7]
    puhelin = (varaus[8])
    sahkoposti = varaus[9]

    print("Varausnumero:",varausnumero)
    print("Varaaja:" , varaaja)
    print("Päivämäärä:", suomalainenPaiva)
    print("Aloitusaika:",suomalainenAika)
    print("Tuntimäärä:", tuntimaara)
    print("Tuntihinta:", tuntihinta,"€")
    print("Kokonaishinta", kokonaishinta,"€")
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
    print("Kohde:", kohde)
    print("Puhelin:", puhelin)
    print("Sähköposti:", sahkoposti)


    #print(suomalainenAika)
    #print(suomalainenPaiva)
    #print(tuntimaara)
    #print("Kokonaishinta:",kokonaishinta)
    #print(maksettu)
    #print(kohde)

    #print(type(varausnumero))
    # Tulostetaan varaus konsoliin
    #print(varaus)

    # Kokeile näitä
    #print(varaus.split('|'))
    #varausId = varaus.split('|')[0]
    #print(varausId)
    #print(type(tuntimaara))
    """
    Edellisen olisi pitänyt tulostaa numeron 123, joka
    on oletuksena tekstiä.

    Voit kokeilla myös vaihtaa kohdan [0] esim. seuraavaksi [1]
    ja testata mikä muuttuu
    """

if __name__ == "__main__":
    main()