from pathlib import Path
import json
from collections import OrderedDict

STORAGE_PATH = 'storage'
BLOCKCHAIN_PATH = 'storage/blockchain'
OPEN_TXS_PATH = 'storage/open_txs'

default_blockchain = [{
    'checkhash': 'genesis',
    'txs': [],
    'type': 'genesis',
    'pow_num': 100,
}]


def make_storage_directories():
    """ Make empty storage directories """
    if not Path(STORAGE_PATH).exists():
        Path(STORAGE_PATH).mkdir(parents=True, exist_ok=True)


def write_blockchain(blockchain):
    """ Write blockchain to disk """

    try:
        with open(BLOCKCHAIN_PATH, mode='w') as blockchainFile:
            blockchainFile.write(json.dumps(blockchain))
    except IOError:
        print('Could not write blockchain.')


def read_blockchain():
    """ Read blockchain from disk """
    if not Path(BLOCKCHAIN_PATH).exists():
        return default_blockchain
    try:
        with open(BLOCKCHAIN_PATH, mode='r') as blockchainFile:
            blockchainString = blockchainFile.readlines()
    except IOError:
        print('Could not read blockchain from disk.')
        return default_blockchain

    return json.loads(blockchainString[0], object_pairs_hook=OrderedDict)


def write_open_txs(open_txs):
    """ Write blockchain to disk """
    try:
        with open(OPEN_TXS_PATH, mode='w') as openTxsFile:
            openTxsFile.write(json.dumps(open_txs))
    except IOError:
        print('Could not read open txs from disk.')
