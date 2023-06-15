from flask import Flask, jsonify
from flask_cors import CORS
from classes.blockchain import Blockchain

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def get_ui():
    return ''


@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    c = Blockchain().blockchain
    result = [block.__dict__.copy() for block in c]
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
