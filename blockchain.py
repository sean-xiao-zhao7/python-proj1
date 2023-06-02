new_tx_amount = float(input('Enter initial TX amount: '))
blockchain = [new_tx_amount]


def get_last_block():
    """get last value of blockchain"""
    return blockchain[-1]


def add_block(tx_amount, last_block):
    """add a single block"""
    blockchain.append([last_block, tx_amount])


while True:
    new_tx_amount = float(input('Enter next TX amount: '))
    if (new_tx_amount):
        add_block(last_block=get_last_block(), tx_amount=new_tx_amount)
        print(blockchain)
