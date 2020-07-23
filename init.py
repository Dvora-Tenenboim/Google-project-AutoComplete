from string import punctuation
from heapq import nsmallest
from collections import defaultdict
import os

MAX_LENGTH_OF_SUBSTRING=10

# def get_k_values(_values,files_map):
#     _values.sort(key=lambda x: x[0])
#     str_list=[]
#     i=_values[0][0]
#     my_file = open(files_map[i])
#     data_list = my_file.read().split("\n")
#     for _value in _values:
#         if _value[0] != i:
#             i=_value[0]
#             my_file = open(files_map[_value[0]])
#             data_list = my_file.read().split("\n")
#         str_list.append((_value, data_list[_value[1]]))


    # str_list=nsmallest(5, str_list, key=lambda e: e[1])
    # return [x[0] for x in str_list]

def clean(my_string):
    exclude = set(punctuation)
    my_string=''.join(ch for ch in my_string if ch not in exclude).lower() #remove punctuation and turn
    return (' '.join(my_string.split())).strip() #remove unnecessary spaces

def getSubStr(_str):
    return set([_str[i:j] for i in range(len(_str)) for j in range(i+1,min(i+MAX_LENGTH_OF_SUBSTRING+1,len(_str)+1)) if _str[i] != " "])

def init_data_collection(map_files):
    map_substrings = defaultdict(list)
    for file_id,file_path in map_files.items():
        with open(file_path,encoding="utf8") as my_file:
            sentences = my_file.read().split("\n")
            for line, sentence in enumerate(sentences):
                substrings=getSubStr(clean(sentence))
                for subStr in substrings:
                    if len(map_substrings[subStr])<5:
                        map_substrings[subStr].append((file_id,line))


    # for key in map_substrings.keys():
    #     map_substrings[key] = get_k_values(map_substrings[key], files_map)

    return map_substrings

def init_map_files(path):
    map_files = {}
    for root, dirs, files in os.walk(path):
        for file_id,file_name in enumerate(files):
            map_files[file_id]=(os.path.join(root, file_name))
    return map_files





