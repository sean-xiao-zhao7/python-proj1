class Block:
    def __init__(self, checkhash, txs, pow_num):
        self.chechhash = checkhash
        self.txs = txs
        self.pow_num = pow_num

    @staticmethod
    def get_genesis_block(self):
        return {
            'checkhash': 'genesis',
            'txs': [],
            'type': 'genesis',
            'pow_num': 100,
        }

    def __repr__(self):
        return self.txs
