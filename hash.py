def reverse_and_push(block, i):
    if i % 2 == 0:
        block.reverse()
    pre = display_bits(block)
    pre = int(pre, 2)
    pre >>= 20
    bin = "{0:b}".format(pre)
    dl = len(bin)
    if dl < 128:
        for z in range(128 - dl):
            bin = '0' + bin
    pre = []
    for z in range(len(bin)):
        pre.append(int(bin[z]))
    return pre


def change_to_hash(plaintext, key, block_size):
    newHash = []
    newHash.extend(key)
    for i in range(len(plaintext) / block_size + 1):
        start = i * block_size
        if start >= len(plaintext):
            break
        end = min(len(plaintext), (i + 1) * block_size)
        block = plaintext[start:end]
        end = end - start
        while end < 128:
            block.append(0)
            end = end + 1
        pre = newHash
        pre = reverse_and_push(pre, i)
        m = [int(block[j] != pre[j]) for j in range(len(pre))]
        newHash = m
    return newHash


###################
# Utility functions that you might find useful

BITS = ('0', '1')
ASCII_BITS = 8


def display_bits(b):
    """converts list of {0, 1}* to string"""
    return ''.join([BITS[e] for e in b])


def seq_to_bits(seq):
    return [0 if b == '0' else 1 for b in seq]


def pad_bits(bits, pad):
    """pads seq with leading 0s up to length pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits


def convert_to_bits(n):
    """converts an integer `n` to bit array"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [(n % 2)] + result
        n = n / 2
    return result


def string_to_bits(s):
    def chr_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)

    return [b for group in
            map(chr_to_bit, s)
            for b in group]


def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return chr(value)


def list_to_string(p):
    return ''.join(p)


def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS])
                    for i in range(0, len(b), ASCII_BITS)])


def pad_bits_append(small, size):
    # as mentioned in lecture, simply padding with
    # zeros is not a robust way way of padding
    # as there is no way of knowing the actual length
    # of the file, but this is good enough
    # for the purpose of this exercise
    diff = max(0, size - len(small))
    return small + [0] * diff


def hashowanie():
    key = string_to_bits('shdfgneykldjksie')
    plaintext = string_to_bits("In cryptograph, a mode of operation is an algorithm that uses a block cipher to provide an information service such as confidentiality or authenticity.")

    newHash = change_to_hash(plaintext, key, 128)

    print newHash
    print bits_to_string(newHash)


hashowanie()