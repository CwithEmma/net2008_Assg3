from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/interfaces')
def interfaces():
    interfaces = {}

    with open('interfaces.txt', 'rt') as file:
        for line in file:
            link = line.find('Link ')
            if (link != -1):
                linky = line.split()

            k = line.find('addr:')
            if (k != -1):
                conv = line[k:].split()[0].split(':')[1]

            interfaces[linky[0]] = conv

    res = make_response(jsonify(interfaces), 200)
    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


