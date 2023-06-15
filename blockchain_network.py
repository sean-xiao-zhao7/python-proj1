from flask import Flask
from flask_cors import CORS
from classes.blockchain import Blockchain

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def get_ui():
    return ''


@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    return Blockchain()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
