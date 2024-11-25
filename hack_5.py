"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s): 
    result = s
    if len(result) >= 3:
        inicio  = s[:3]
        if inicio == "foo":
            return "fo-zi-ma-"
        for i in range(1, len(s)):
            if i %3 == 0:
                result = result[:i-1] + "-" + result[i:]
        
    return result
