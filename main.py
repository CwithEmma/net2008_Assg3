from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

app.register_error_handler(400, handle_bad_request)
