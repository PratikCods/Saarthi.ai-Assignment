d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}


def merge_dictionary(d1,d2):
    if len(d1) < len(d2):  #for reducing time complexity,chose list with larger number of elements
        d1,d2 = d2,d1
    new_dictionary = d1.copy()   #makes copy of the larger dictionary
    for key,value in d2.items():
        if key in d1.keys():
            new_dictionary[key] = new_dictionary[key] + value
        else:
            new_dictionary[key] = value

    return new_dictionary

for key,value in merge_dictionary(d1,d2).items():
    print(key,':',value)