# codewars challenge
# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001




def split_into_pairs(string):
    pairs = []
    for i in range(0, len(string), 2):
        if i + 1 < len(string):
            pairs.append(string[i:i+2])
        else:
            pairs.append(string[i] + '_')
    return pairs

print(split_into_pairs('abc'))     # ['ab', 'c_']
print(split_into_pairs('abcdef'))  # ['ab', 'cd', 'ef']