import mysql.connector
from geopy.distance import geodesic


def yhdista_tietokantaan():
    return mysql.connector.connect(
        host='localhost',
        port=3306,
        database='lentokonepeli',
        user='root',
        password='1234'
    )


def hae_koordinaatit(yhteys, icao):
    kursori = yhteys.cursor()
    kursori.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'")
    return kursori.fetchone()


def main():
    yhteys = yhdista_tietokantaan()

    icao1 = input('Syötä ensimmäisen lentokentän ICAO-koodi: ')
    icao2 = input('Syötä toisen lentokentän ICAO-koodi: ')

    koord1 = hae_koordinaatit(yhteys, icao1)
    koord2 = hae_koordinaatit(yhteys, icao2)

    if koord1 and koord2:
        etaisyys = geodesic(koord1, koord2).kilometers
        print(f'Lentokenttien välinen etäisyys on {etaisyys:.2f} km.')



main()
