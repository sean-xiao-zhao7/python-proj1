

def write_blockchain(blockchain, open_txs):
    """ Write blockchain to disk """
    with open('storage/blockchain', mode='w') as blockchainFile:
        blockchainFile.write(str(blockchain))
        blockchainFile.write('\n')
        blockchainFile.write(str(open_txs))
