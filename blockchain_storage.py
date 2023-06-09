from pathlib import Path

BLOCKCHAIN_PATH = 'storage/blockchain'
OPEN_TXS_PATH = 'storage/open_txs'


def write_blockchain(blockchain):
    """ Write blockchain to disk """
    Path(BLOCKCHAIN_PATH).mkdir(parents=True, exist_ok=True)
    with open(BLOCKCHAIN_PATH, mode='w') as blockchainFile:
        blockchainFile.write(str(blockchain))


def write_open_txs(open_txs):
    """ Write blockchain to disk """
    Path(OPEN_TXS_PATH).mkdir(parents=True, exist_ok=True)
    with open(OPEN_TXS_PATH, mode='w') as openTxsFile:
        openTxsFile.write(str(open_txs))
