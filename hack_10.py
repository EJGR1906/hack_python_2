"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""

def fn_hack_10(s):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for item in s:
        if isinstance(item, dict):
            key, value = list(item.items())[0]
            result.append({str(abc.index(key) + 1): str(abc.index(value) + 1)})
        
        elif isinstance(item, set):
            set_list = list(item)
            result.append({str(abc.index(set_list[0]) + 1), str(abc.index(set_list[1]) + 1)})
        
    return result
  