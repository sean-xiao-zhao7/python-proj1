from collections import OrderedDict
from blockchain_hashlib import generate_hash, verify_proof
from blockchain_storage import write_blockchain, write_open_txs, make_storage_directories, read_blockchain

MINING_REWARD = 5.0
blockchain = []
global_open_txs = []
global_sender = "test_sender"
global_sender_balance = 10
users = {global_sender}


def get_last_block():
    """get last value of blockchain"""
    return blockchain[-1]


def add_block(recipient, tx_amount=1):
    """add a single block"""
    global users, global_sender_balance

    if float(tx_amount) > global_sender_balance:
        return "Not enough balance."

    if not verify_blockchain():
        return False

    mine_block(recipient, tx_amount)
    users.add(recipient)
    global_sender_balance -= float(tx_amount)
    return True


def mine_block(recipient, tx_amount):
    """ Mine a block """
    global global_open_txs
    global_open_txs_copy = global_open_txs[:]

    global_open_txs_copy.extend([
        OrderedDict([("sender", global_sender), ("recipient",
                    recipient), ("tx_amount", float(tx_amount)), ("type", "mine")]),
        OrderedDict([("sender", None), ("recipient", global_sender),
                    ("tx_amount", MINING_REWARD), ("type", "reward")])

    ])

    # hashing
    # new_checkhash = str(get_last_block().values())
    new_checkhash = generate_hash(get_last_block())

    global_open_txs = global_open_txs_copy

    # Do POW
    pow_num = generate_pow()

    blockchain.append({
        "checkhash": new_checkhash,
        "txs": global_open_txs,
        "pow_num": pow_num
    })

    global_open_txs = []


def generate_pow():
    """ Generate proof of work. """
    current_chechhash = generate_hash(get_last_block())
    current_proof_num = 0
    while not verify_proof(global_open_txs, current_chechhash, current_proof_num):
        current_proof_num += 1
    return current_proof_num


def verify_blockchain():
    """ Make sure checkhash matches actual previous block content  """
    prev_block = None
    for block in blockchain:
        if not prev_block:
            prev_block = block
            continue
        else:
            if not generate_hash(prev_block) == block["checkhash"]:
                return False
            if not verify_proof(block["txs"], block["checkhash"], block["pow_num"]):
                return False
            prev_block = block
    return True


def print_blockchain():
    """ Pretty print """
    for index, block in enumerate(blockchain):
        print(index, block["txs"])
        print("---")


def get_balance(username):
    """ Print balance of a single user """
    balance = 0
    for block in blockchain:
        for tx in block["txs"]:
            if tx["sender"] == username or tx["recipient"] == username:
                balance += tx["tx_amount"]
    return balance


if __name__ == '__main__':

    make_storage_directories()
    # read blockchain from disk if exists
    blockchain = read_blockchain()
    print("Blockchain loaded from disk.")
    print_blockchain()

    while True:
        user_input = input("Enter next TX amount or command: ")

        # string value entered
        if not user_input.isdigit():
            if user_input == "q" or user_input == "quit":
                break
            elif user_input == "b" or user_input == "balance":
                username = input("Enter username:")
                if username:
                    print(get_balance(username))
            continue

        # numeric value entered
        new_tx_amount = float(user_input)
        new_tx_recipient = input("Enter recipient:")
        if new_tx_amount and new_tx_recipient:
            if not blockchain:
                pass
            else:
                result = add_block(new_tx_recipient, new_tx_amount)
                if result == "Not enough balance.":
                    print(
                        f"Your balance of {global_sender_balance} is not enough to send {new_tx_amount}")
                    continue
                elif result == False:
                    print("Blockchain cannot be verified. Exiting.")
                    break

            print_blockchain()

            # write to disk
            write_blockchain(blockchain)
            write_open_txs(global_open_txs)
        else:
            print("Invalid amount entered.")
