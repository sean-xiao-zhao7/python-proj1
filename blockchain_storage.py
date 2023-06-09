from pathlib import Path

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
    if not Path.exists(STORAGE_PATH):
        Path(STORAGE_PATH).mkdir(parents=True, exist_ok=True)


def write_blockchain(blockchain):
    """ Write blockchain to disk """

    with open(BLOCKCHAIN_PATH, mode='w') as blockchainFile:
        blockchainFile.write(str(blockchain))


def read_blockchain():
    """ Read blockchain from disk """
    if not Path.exists(BLOCKCHAIN_PATH):
        return default_blockchain

    with open(BLOCKCHAIN_PATH, mode='r') as blockchainFile:
        blockchain = blockchainFile.readlines()

    return blockchain


def write_open_txs(open_txs):
    """ Write blockchain to disk """
    with open(OPEN_TXS_PATH, mode='w') as openTxsFile:
        openTxsFile.write(str(open_txs))
