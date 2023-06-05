import numbers
blockchain = []
open_txs = []


def get_last_block():
    """get last value of blockchain"""
    return blockchain[-1]


def add_block(sender, recipient, tx_amount=1):
    """add a single block"""
    open_txs.append({
        'sender': sender,
        'recipient': recipient,
        'tx_amount': tx_amount
    })


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
            pass
        else:
            pass
        print(blockchain)
