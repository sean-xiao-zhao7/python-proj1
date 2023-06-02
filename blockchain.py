blockchain = [0]


def last_block():
    """get last value of blockchain"""
    return blockchain[-1]


def add_value(tx_amount, last_tx_amount=last_block()):
    """add a single block"""
    blockchain.append([last_tx_amount, tx_amount])


add_value(1)
add_value(2)
add_value(3)
print(blockchain)
