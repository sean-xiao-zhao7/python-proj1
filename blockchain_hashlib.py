import hashlib
import json


def generate_hash(block_dict):
    """ Generate a secure hash for checkhash """
    return hashlib.sha256(json.dumps(
        block_dict.__dict__.copy(), sort_keys=True).encode()).hexdigest()


def verify_proof(txs, last_checkhash, proof_num):
    """ Verify current proof is valid. """
    guess = (str(txs) + str(last_checkhash) + str(proof_num)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[:2] == '00'
