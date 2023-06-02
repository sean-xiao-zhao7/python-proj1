blockchain = [0]


def add_value(tx_amount):
    blockchain.append([blockchain[-1], 5.3])
    print(blockchain)


add_value(1)
add_value(2)
add_value(3)
