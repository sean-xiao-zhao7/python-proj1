from pathlib import Path
import json
from collections import OrderedDict
from classes.block import Block

STORAGE_PATH = 'storage'
BLOCKCHAIN_PATH = 'storage/blockchain'
OPEN_TXS_PATH = 'storage/open_txs'
PEER_NODES_PATH = 'storage/peer_nodes'

default_blockchain = [
    Block.get_genesis_block()
]


def make_storage_directories():
    """ Make empty storage directories """
    if not Path(STORAGE_PATH).exists():
        Path(STORAGE_PATH).mkdir(parents=True, exist_ok=True)


def write_blockchain(blockchain):
    """ Write blockchain to disk """

    try:
        with open(BLOCKCHAIN_PATH, mode='w') as blockchainFile:
            blockchainFile.write(json.dumps(blockchain, default=lambda o: o.__dict__,
                                            ))
    except IOError:
        print('Could not write blockchain.')


def read_blockchain():
    """ Read blockchain from disk """
    if not Path(BLOCKCHAIN_PATH).exists():
        print('No blockchain on disk. Initialized new blockchain.')
        return default_blockchain
    try:
        with open(BLOCKCHAIN_PATH, mode='r') as blockchainFile:
            blockchainString = blockchainFile.readlines()
    except IOError:
        print('Error reading blockchain from disk.')
        return default_blockchain
    if not blockchainString:
        print('No blockchain on disk. Initialized new blockchain.')
        return default_blockchain
    print("Blockchain loaded from disk.")

    # change dict to Block
    blockchainDictList = json.loads(
        blockchainString[0], object_pairs_hook=OrderedDict)
    blockchainBlockList = []
    for blockDict in blockchainDictList:
        blockchainBlockList.append(Block(
            blockDict['checkhash'], blockDict['txs'], blockDict['type'], blockDict['pow_num']))

    return blockchainBlockList


def write_open_txs(open_txs):
    """ Write blockchain to disk """
    try:
        with open(OPEN_TXS_PATH, mode='w') as openTxsFile:
            openTxsFile.write(json.dumps(open_txs))
    except IOError:
        print('Could not write open txs to disk.')


def write_peer_nodes(peer_nodes):
    """ Write peer nodes to disk """
    try:
        with open(PEER_NODES_PATH, mode='w') as peerNodesFile:
            peerNodesFile.write(json.dumps(peer_nodes))
    except IOError:
        print('Could not write peer nodes to disk.')
