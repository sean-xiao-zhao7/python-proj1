class Block:
    def __init__(self, checkhash, txs, pow_num):
        self.chechhash = checkhash
        self.txs = txs
        self.pow_num = pow_num

    def __repr__(self):
        return self.txs
