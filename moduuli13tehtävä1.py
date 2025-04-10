from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/prime/<luku>')
def prime(luku):

    status = 200

    try:
        isPrime = True

        luku = int(luku)

        for i in range(2, luku):
            if luku % i == 0:
                isPrime = False
                break

        answer = {
            'number': luku,
            'status': status,
            'isPrime': isPrime
        }

    except ValueError:
        answer = {
            'number' : luku,
            'status' : 400,
            'kuvaus' : 'ValueError tapahtui :('
        }

    json_answer = json.dumps(answer)
    return Response(response=json_answer, status=status, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


#plspushp
