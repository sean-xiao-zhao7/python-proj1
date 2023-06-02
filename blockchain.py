blockchain = [0]


def last_value():
    """get last value of blockchain"""
    return blockchain[-1]


def add_value(tx_amount):
    """add a single block"""
    blockchain.append([last_value(), tx_amount])
    print(blockchain)


add_value(1)
add_value(2)
add_value(3)
