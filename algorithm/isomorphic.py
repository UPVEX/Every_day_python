# is isomorphic?
# foo , bar -> false
# foo , bee -> true
# fow , bee -> false



def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    dict = {}
    set_values = set()

    for i in range(len(s)):

        if s[i] not in dict:

            if t[i] in set_values:
                return False
            dict[s[i]] = t[i]
            set_values.add(t[i])

        else:
            if dict[s[i]] != t[i]:
                return False
    return True        

print(is_isomorphic('for' ,'bet'))