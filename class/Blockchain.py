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

    def __repr__(self):
        for index, block in enumerate(self.blockchain):
            print(index, block)
            print("---")
