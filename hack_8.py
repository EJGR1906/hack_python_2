"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    s_length = len(s)
    if s_length % 2 == 0:
        result = [str(s_length - i) for i in range(s_length)]
    else:
        result = [f"{s[s_length - i - 1]}-{s_length - i}" for i in range(s_length)]
    
    return result


