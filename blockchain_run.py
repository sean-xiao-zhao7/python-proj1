from classes.blockchain import Blockchain

if __name__ == '__main__':

    blockchain = Blockchain()
    print(blockchain)

    while True:
        user_input = input("Enter next TX amount or command: ")

        # string value entered
        if not user_input.isdigit():
            if user_input == "q" or user_input == "quit":
                break
            elif user_input == "b" or user_input == "balance":
                username = input("Enter username:")
                if username:
                    print(blockchain.get_balance(username))
            continue

        # numeric value entered
        new_tx_amount = float(user_input)
        new_tx_recipient = input("Enter recipient:")
        if new_tx_amount and new_tx_recipient:
            if blockchain.is_empty():
                pass
            else:
                result = blockchain.add_block(new_tx_recipient, new_tx_amount)
                if result == "Not enough balance.":
                    print(
                        f"Your balance of {blockchain.global_sender_balance} is not enough to send {new_tx_amount}")
                    continue
                elif result == False:
                    print("Blockchain cannot be verified. Exiting.")
                    break

            print(blockchain)

            # write to disk
            blockchain.save_blockchain_disk()
        else:
            print("Invalid amount entered.")
