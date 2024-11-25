"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""

def fn_hack_2(s):
    vowels = "aeiou"
    result = "".join([char for char in s if char not in vowels])
    return result



