# codewars challenge
# https://www.codewars.com/kata/5254ca2719453dcc0b00027d



def generate_permutations(s):
    if len(s) == 1:
        return [s]

    result = set()
    for i in range(len(s)):
        first_char = s[i]
        rest_chars = s[:i] + s[i+1:]
        for perm in generate_permutations(rest_chars):
            result.add(first_char + perm)

    return list(result)

print(generate_permutations('a'))  # ['a']
print(generate_permutations('ab'))  # ['ab', 'ba']
print(generate_permutations('abc'))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(generate_permutations('aabb'))  # ['aabb', 'abab', 'abba', 'bbaa', 'baba', 'baab']



# second method

'''
import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))

'''