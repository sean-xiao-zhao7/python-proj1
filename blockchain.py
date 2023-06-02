blockchain = [0]


def get_last_block():
    """get last value of blockchain"""
    return blockchain[-1]


def add_block(tx_amount, last_block):
    """add a single block"""
    blockchain.append([last_block, tx_amount])


add_block(1, get_last_block())
add_block(2, get_last_block())
add_block(last_block=get_last_block(), tx_amount=3)
print(blockchain)
