import hashlib, time

def get_proof(header, nonce):
    preimage = f"{header}:{nonce}".encode()
    #gives us the string value of a hexadecimal number
    proof_hex = hashlib.sha256(preimage).hexdigest()
    #converts the string into an int
    return int(proof_hex, 16)

def mine(header, target, nonce):
    while (get_proof(header, nonce) >= target):
        nonce += 1
    return nonce

def mining_demo(header):
    previous_nonce = -1
    for difficulty_bits in range(1,30):
        target = 2 ** (256 - difficulty_bits)

        start_time = time.time()
        nonce = mine(header, target, previous_nonce)
        proof = get_proof(header, nonce)
        elapsed_time = time.time() - start_time
        #.0e is to make it standard form
        target_str = f"{target:.0e}"
        elapsed_time_str = f"{elapsed_time:.0e}" if nonce != previous_nonce else ""
        bin_proof_str = f"{proof:0256b}"[:50]

        print(f"bits: {difficulty_bits:>3} target: {target_str:>7} elapsed{elapsed_time_str:>7} nonce:{nonce:>10} proof: {bin_proof_str}...")

        previous_nonce = nonce

if __name__ == "__main__":
    header = "hello"
    # number of leading bits we require
    mining_demo(header)
