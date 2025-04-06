# a1z26
# amir -> [97, 109, 105, 114]
# nima -> [110, 105, 109, 97]


def encode(plain):
    return [ord(elm) for elm in plain]

def decode(encode):
    return "".join(chr(elm) for elm in encode)

print(decode([110, 105, 109, 97]))