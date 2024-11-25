"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""
def fn_hack_1(s):
    txt_ls = [s[i:i+3] for i in range(0, len(s), 3)]
    result = ''.join([txt if len(txt) != 3 else f"{txt[0]}{txt[1].upper()}{txt[2]}" for txt in txt_ls])
    return result

    
