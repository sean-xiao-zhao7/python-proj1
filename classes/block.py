class Block:
    def __init__(self, checkhash, txs, type, pow_num):
        self.chechhash = checkhash
        self.txs = txs
        self.type = type
        self.pow_num = pow_num

    @staticmethod
    def get_genesis_block():
        return Block(
            'genesis',
            [],
            'genesis',
            100,
        )

    def __repr__(self):
        return str(self.txs)
