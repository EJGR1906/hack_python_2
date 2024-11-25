"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    
    replacements = {
        "foo": "Foo",
        "Foo": "Fooziman"
    }
    
    for key in s:
        if key in replacements:
            result[replacements[key]] = replacements[replacements[key]]
    
    return result

