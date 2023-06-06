MINING_REWARD = 5.0
blockchain = [{
    'checkhash': 'genesis',
    'txs': [],
    'type': 'genesis'
}]
global_open_txs = []
global_sender = 'test_sender'
users = {global_sender}


def get_last_block():
    """get last value of blockchain"""
    return blockchain[-1]


def add_block(recipient, tx_amount=1):
    """add a single block"""
    global users

    if not verify_blockchain():
        return False

    mine_block(recipient, tx_amount)
    users.add(recipient)
    return True


def mine_block(recipient, tx_amount):
    """ Mine a block """
    global global_open_txs

    global_open_txs.extend([{
        'sender': global_sender,
        'recipient': recipient,
        'tx_amount': float(tx_amount),
        'type': 'mine'
    }, {
        'sender': None,
        'recipient': global_sender,
        'tx_amount': MINING_REWARD,
        'type': 'reward'
    }])

    new_checkhash = str(get_last_block().values())
    blockchain.append({
        'checkhash': new_checkhash,
        'txs': global_open_txs
    })

    global_open_txs = []


def verify_blockchain():
    """ Make sure checkhash matches actual previous block content  """
    prev_block = None
    for block in blockchain:
        if not prev_block:
            prev_block = block
            continue
        else:
            print(block['checkhash'])
            if not str(prev_block.values()) == block['checkhash']:
                return False
            prev_block = block
    return True


def print_blockchain():
    """ Pretty print """
    for index, block in enumerate(blockchain):
        print(index, block['txs'])
        print('---')


def get_balance(username):
    """ Print balance of a single user """
    balance = 0
    for block in blockchain:
        for tx in block['txs']:
            if tx['sender'] == username or tx['recipient'] == username:
                balance += tx['tx_amount']
    return balance


while True:
    user_input = input('Enter next TX amount or command: ')

    # string value entered
    if not user_input.isdigit():
        if user_input == 'q' or user_input == 'quit':
            break
        elif user_input == 'b' or user_input == 'balance':
            username = input('Enter username:')
            if username:
                print(get_balance(username))
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
