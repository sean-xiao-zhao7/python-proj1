from flask import Flask, jsonify
from flask_cors import CORS
from classes.blockchain import Blockchain

app = Flask(__name__)
CORS(app)
blockchain = Blockchain()


@app.route('/', methods=['GET'])
def get_root():
    return 'Python Proj1 Blockchain', 200


@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    c = blockchain.blockchain
    result = [block.__dict__.copy() for block in c]
    return jsonify(result), 200


@app.route('/add-block', methods=['POST'])
def mine_block():
    blockchain.add_block('test')
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
