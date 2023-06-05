import numbers
blockchain = []
open_txs = []


def get_last_block():
    """get last value of blockchain"""
    return blockchain[-1]


def add_block(tx_amount, last_block):
    """add a single block"""
    blockchain.append([last_block, tx_amount])


def mine_block():
    """ Mine a block """
    pass


while True:
    user_input = input('Enter next TX amount or command: ')

    # string value entered
    if not user_input.isdigit():
        if user_input == 'q':
            break
        else:
            continue

    # numeric value entered
    new_tx_amount = float(user_input)
    if new_tx_amount:
        if not blockchain:
            blockchain.append(new_tx_amount)
        else:
            add_block(last_block=get_last_block(), tx_amount=new_tx_amount)
        print(blockchain)
