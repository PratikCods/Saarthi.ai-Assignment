dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, 
{'name': 'affirm', 'confidence': 0.944814920425415}, 
{'name': 'inform', 'confidence': 0.9842240810394287}, 
{'name': 'inform', 'confidence': 0.9842240810394287}]


def unique_dict(dict):
    key_list = list(dict_list[0].keys())
    first_key = key_list[0]
    return {x[first_key]:x for x in dict_list}.values()

print(unique_dict)
