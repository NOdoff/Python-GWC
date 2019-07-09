from pprint import pprint
def make_words_length_dict(words_list):
    dictionary = {}
    for word in words_list:
        dictionary[word] = len(word)
    return dictionary
def print_all_values(dict):
    # for key, value in dict.items():
    #     print('Key: ', key)
    #     print('Value: ', value)
    for key in dict.keys():
        print( key, ' : ', dict[key])
words =['I', 'am', 'a', 'brilliant', 'computer', 'scientist']
new_dict = make_words_length_dict(words)
pprint(make_words_length_dict(words))
print_all_values(new_dict)

sd = 10
ages = 10
