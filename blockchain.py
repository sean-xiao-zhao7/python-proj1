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
