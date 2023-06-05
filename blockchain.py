import numbers
blockchain = []
open_txs = []
global_sender = 'test_sender'


def get_last_block():
    """get last value of blockchain"""
    return blockchain[-1]


def add_block(recipient, tx_amount=1):
    """add a single block"""
    open_txs.append({
        'sender': global_sender,
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
    new_tx_recipient = input('Enter recipient:')
    if new_tx_amount and new_tx_recipient:
        if not blockchain:
            pass
        else:
            add_block(new_tx_recipient, new_tx_amount)
        print(blockchain)
    else:
        print('Invalid amount entered.')
