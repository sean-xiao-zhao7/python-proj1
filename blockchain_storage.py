from pathlib import Path
from ast import literal_eval

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

    with open(BLOCKCHAIN_PATH, mode='w') as blockchainFile:
        blockchainFile.write(str(blockchain))


def read_blockchain():
    """ Read blockchain from disk """
    if not Path(BLOCKCHAIN_PATH).exists():
        return default_blockchain

    with open(BLOCKCHAIN_PATH, mode='r') as blockchainFile:
        blockchainString = blockchainFile.readlines()

    return literal_eval(blockchainString)


def write_open_txs(open_txs):
    """ Write blockchain to disk """
    with open(OPEN_TXS_PATH, mode='w') as openTxsFile:
        openTxsFile.write(str(open_txs))
