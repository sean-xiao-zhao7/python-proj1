from collections import OrderedDict
from blockchain_hashlib import generate_hash, verify_proof
from blockchain_storage import write_blockchain, write_open_txs, make_storage_directories, read_blockchain
from block import Block


class Blockchain:
    def __init__(self):
        # initiate blockchain and sender data
        self.blockchain = []
        self.global_open_txs = []
        self.global_sender = "test_sender"
        self.global_sender_balance = 10
        self.users = {self.global_sender}

        # read blockchain from disk
        make_storage_directories()
        self.load_blockchain_disk()

    def load_blockchain_disk(self):
        self.blockchain = read_blockchain()
        print("Blockchain loaded from disk.")

    def save_blockchain_disk(self):
        write_blockchain(self.blockchain)
        write_open_txs(self.global_open_txs)

    def get_last_block(self):
        """get last value of blockchain"""
        return self.blockchain[-1]

    def add_block(recipient, tx_amount=1):
        """add a single block"""
        if float(tx_amount) > self.global_sender_balance:
            return "Not enough balance."

        if not self.verify_blockchain():
            return False

        self.mine_block(recipient, tx_amount)
        self.users.add(recipient)
        self.global_sender_balance -= float(tx_amount)
        return True

    def mine_block(recipient, tx_amount):
        """ Mine a block """
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

    def get_balance(username):
        """ Print balance of a single user """
        balance = 0
        for block in blockchain:
            for tx in block["txs"]:
                if tx["sender"] == username or tx["recipient"] == username:
                    balance += tx["tx_amount"]
        return balance

    def __repr__(self):
        for index, block in enumerate(self.blockchain):
            print(index, block)
            print("---")
