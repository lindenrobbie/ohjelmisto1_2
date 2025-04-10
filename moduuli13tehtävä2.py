from flask import Flask, Response
import json
import mysql.connector

def connect():
    return mysql.connector.connect(
        host='localhost',
        port=3306,
        database='lentokonepeli',
        user='root',
        password='root'
    )

def get_airport_data(connection, icao):
    cursor = connection.cursor()
    cursor.execute(f"SELECT name, municipality FROM airport WHERE ident = '{icao}'")
    return cursor.fetchone()

app = Flask(__name__)
@app.route('/airport/<icao>')

def airport(icao):

    status = 200

    try:

        connection = connect()

        result = get_airport_data(connection, icao)

        if result:
            name, municipality = result
            answer = {
                'ICAO': icao,
                'Name': name,
                'Municipality': municipality,
                'Status': status,
            }
        else:
            status = 404
            answer = {
                'Status' : status,
                'Virhe': f"Lentokenttä ICAO koodilla {icao} ei löydy."
            }


    except ValueError:
        answer = {
            'ICAO': icao,
            'Name': name,
            'Municipality': municipality,
            'Status': 400,
        }

    json_answer = json.dumps(answer)
    return Response(response=json_answer, status=status, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


#plspushp
