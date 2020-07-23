from auto_complete_data import AutoCompleteData
import fix

COMPLETIONS_NUM=5

index_score_action_list=[((4,-1),1,"change"), ((3,3),2,"change"),((4,-1),2,"add_or_delete"),((2,2),3,"change"),
((3,3),4,"add_or_delete"), ((1,1),4,"change"), ((0,0),5,"change"), ((2,2),6,"add_or_delete"),((1,1),8,"add_or_delete"),
((0,0),10,"add_or_delete")]


def read_sentence_from_file(file_path, num_line):
    with open(file_path) as my_file:
        sentences = my_file.read().split("\n")
        return sentences[num_line]

def sort_by_score(auto_complete_list):
    return sorted(auto_complete_list,key=lambda a: a.score)

def is_enoughf(set_options):
    return len(set_options)>=COMPLETIONS_NUM

def get_auto_complete_list(map_files, substring, list_file_id_file_line, less_score=0):
    auto_complete_list=[]
    for curr_file_id,curr_line in list_file_id_file_line:
        file_path=map_files[curr_file_id]
        sentence=read_sentence_from_file(file_path, curr_line)
        auto_complete_list.append(AutoCompleteData(sentence, substring,file_path, curr_line, less_score))
    return auto_complete_list

def get_best_k_completions(substring, map_substring, map_files):
    auto_complete_best_options=[]
    list_best_options = map_substring.get(substring, [])
    auto_complete_best_options=get_auto_complete_list(map_files, substring, list_best_options)
    for start_end, score, action in index_score_action_list:
        if action=="change":
            list_best_options = list(set(list_best_options+fix.get_changed_char_options(substring, map_substring, start_end[0], start_end[1])))
        elif action=="add_or_delete":
            list_best_options = list(set(list_best_options + fix.get_add_or_remove_char_options(substring, map_substring, start_end[0], start_end[1])))
        auto_complete_best_options += get_auto_complete_list(map_files, substring, list_best_options,score)
        if is_enoughf(auto_complete_best_options):
            return sort_by_score(auto_complete_best_options)[:5]
    return sort_by_score(auto_complete_best_options)[:5]
    return auto_complete_best_options



