blockchain = [{
    'checkhash': 'genesis',
    'txs': []
}]
global_open_txs = []
global_sender = 'test_sender'


def get_last_block():
    """get last value of blockchain"""
    return blockchain[-1]


def add_block(recipient, tx_amount=1):
    """add a single block"""
    if not verify_blockchain():
        return False

    global_open_txs.append({
        'sender': global_sender,
        'recipient': recipient,
        'tx_amount': tx_amount
    })
    mine_block()


def mine_block():
    """ Mine a block """
    global global_open_txs
    new_checkhash = str(get_last_block().values())

    blockchain.append({
        'checkhash': new_checkhash,
        'txs': global_open_txs
    })
    global_open_txs = []


def verify_blockchain():
    """ Make sure checkhash matches actual previous block content  """
    return False


def print_blockchain():
    """ Pretty print """
    for index, block in enumerate(blockchain):
        print(index, block)


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
            if not add_block(new_tx_recipient, new_tx_amount):
                print('Blockchain cannot be verified. Exiting.')
                break
        print_blockchain()
    else:
        print('Invalid amount entered.')
