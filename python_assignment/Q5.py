import itertools
#Modify the Entities_list and Utterance_list to provide input data
Entities_list = ["     kolkata", "delhi","mumbai","kolkata   "]
Utterance_list = ["How far is <> from <>    ", "How is the weather in <>","From <> to <> to <>"]

def data_cleanup(data_list):    #incase provided list contains any trailing whitespaces or redundant data
    data_list = [str.strip() for str in data_list]
    data_list = list(set(data_list)) 
    return data_list

def generate_utterances(entity_list,utterance_list):
    entity_list = data_cleanup(entity_list)
    utterance_list = data_cleanup(utterance_list)
    res_list = []
    for str in utterance_list:
        null_count = str.count("<>") #counts <> in the utterance list
        entity_permutations = list(itertools.permutations(entity_list,null_count)) #generates all possible permutations of the entities
        for permutation in entity_permutations: #iterating through the permutations list
            temp_str = str[:]
            for entity in permutation: #replacing <> one at a time for each entity in the permutation
                temp_str = temp_str.replace('<>',entity,1)
            res_list.append(temp_str)
    return res_list
        
all_unique_utterances = generate_utterances(Entities_list,Utterance_list)
print(all_unique_utterances)