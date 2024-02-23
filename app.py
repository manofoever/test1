from flask import Flask
from tokenRequest import *

app = Flask(__name__)

@app.route('/ask_me_1')
def get_json_data():
    result = tokenRequest("http://54.224.122.233:5000/ask_me")
    return result.request_token()


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)