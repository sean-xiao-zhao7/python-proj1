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
        self.mining_reward = 5.0

        # read blockchain from disk
        make_storage_directories()
        self.load_blockchain_disk()

    def is_empty(self):
        return not self.blockchain

    def load_blockchain_disk(self):
        self.blockchain = read_blockchain()
        for block in self.blockchain:
            print(block)
        print("Blockchain loaded from disk.")

    def save_blockchain_disk(self):
        write_blockchain(self.blockchain)
        write_open_txs(self.global_open_txs)

    def get_last_block(self):
        """get last value of blockchain"""
        return self.blockchain[-1]

    def add_block(self, recipient, tx_amount=1):
        """add a single block"""
        if float(tx_amount) > self.global_sender_balance:
            return "Not enough balance."

        if not self.verify_blockchain():
            return False

        self.mine_block(recipient, tx_amount)
        self.users.add(recipient)
        self.global_sender_balance -= float(tx_amount)
        return True

    def mine_block(self, recipient, tx_amount):
        """ Mine a block """
        global_open_txs_copy = self.global_open_txs[:]

        global_open_txs_copy.extend([
            OrderedDict([("sender", self.global_sender), ("recipient",
                        recipient), ("tx_amount", float(tx_amount)), ("type", "mine")]),
            OrderedDict([("sender", None), ("recipient", self.global_sender),
                        ("tx_amount", self.mining_reward), ("type", "reward")])

        ])

        # hashing
        # new_checkhash = str(self.get_last_block().values())
        new_checkhash = generate_hash(self.get_last_block())

        self.global_open_txs = global_open_txs_copy

        # Do POW
        pow_num = self.generate_pow()

        self.blockchain.append(Block(
            new_checkhash,
            self.global_open_txs,
            pow_num
        ))

        self.global_open_txs = []

    def generate_pow(self):
        """ Generate proof of work. """
        current_chechhash = generate_hash(self.get_last_block())
        current_proof_num = 0
        while not verify_proof(self.global_open_txs, current_chechhash, current_proof_num):
            current_proof_num += 1
        return current_proof_num

    def verify_blockchain(self):
        """ Make sure checkhash matches actual previous block content  """
        prev_block = None
        for block in self.blockchain:
            if not prev_block:
                prev_block = block
                continue
            else:
                if not generate_hash(prev_block) == block.checkhash:
                    return False
                if not verify_proof(block.txs, block.checkhash, block.pow_num):
                    return False
                prev_block = block
        return True

    def get_balance(self, username):
        """ Print balance of a single user """
        balance = 0
        for block in self.blockchain:
            for tx in block.txs:
                if tx["sender"] == username or tx["recipient"] == username:
                    balance += tx["tx_amount"]
        return balance

    def __repr__(self):
        for index, block in enumerate(self.blockchain):
            print(index, block)
            print("---")
