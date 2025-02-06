import mysql.connector

print("")

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='lentokonepeli',
         user='robbie',
         password='lol',
         autocommit=True,
         collation='utf8mb3_unicode_ci')

def main():

    while True:

        tablerequest = input('Syötä tähän ICAO koodi: ')
        sql = f"SELECT airport.name FROM airport WHERE airport.ident = '{tablerequest}';"
        print("")

        if sql == '':
            break

        else:

            with yhteys.cursor() as kursori:
                kursori.execute(sql)

                tulos = kursori.fetchall()

                if kursori.rowcount >0:
                    for rivi in tulos:
                        print(f'Output: {rivi[0]}')
                        print("")
                else:
                    print(f'Syöttämäsi ICAO koodilla {tablerequest} ei löytynyt tulosta.')
                    print("")

main()
