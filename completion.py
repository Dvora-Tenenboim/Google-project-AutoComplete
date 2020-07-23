from auto_complete_data import AutoCompleteData
from revised_options import get_changed_char_options, get_add_or_remove_char_options

COMPLETIONS_NUM = 5
CHANGE = "change"
ADD_OR_DELETE = "add_or_delete"

index_score_action_list = [((4, -1), 1, CHANGE), ((3, 3), 2, CHANGE), ((4, -1), 2, ADD_OR_DELETE), ((2, 2), 3, CHANGE),
                           ((3, 3), 4, ADD_OR_DELETE), ((1, 1), 4, CHANGE), ((0, 0), 5, CHANGE),
                           ((2, 2), 6, ADD_OR_DELETE), ((1, 1), 8, ADD_OR_DELETE),
                           ((0, 0), 10, ADD_OR_DELETE)]


def read_sentence_from_file(file_path, num_line):
    with open(file_path) as my_file:
        sentences = my_file.read().split("\n")
        return sentences[num_line]


def is_enough(set_options):
    return len(set_options) >= COMPLETIONS_NUM


def get_auto_complete_list(map_files, substring, list_file_id_file_line, less_score=0):
    auto_complete_list = []
    for curr_file_id, curr_line in list_file_id_file_line:
        file_path = map_files[curr_file_id]
        sentence = read_sentence_from_file(file_path, curr_line)
        auto_complete_list.append(AutoCompleteData(sentence, substring, file_path, curr_line, less_score))
    return auto_complete_list


def get_best_k_completions(substring, map_substring, map_files):
    list_best_options = map_substring.get(substring, [])
    auto_complete_best_options = get_auto_complete_list(map_files, substring, list_best_options)
    if not is_enough(auto_complete_best_options):
        for start_end, score, action in index_score_action_list:
            new_best_options=[]
            if action == CHANGE:
                new_best_options = list(set(get_changed_char_options(substring,
                                                                     map_substring,start_end[0],
                                                                     start_end[1])) - set(list_best_options))
            elif action == ADD_OR_DELETE:
                new_best_options = list(set(get_add_or_remove_char_options(substring,
                                                                           map_substring, start_end[0],
                                                                           start_end[1])) - set(list_best_options))
            list_best_options += new_best_options
            auto_complete_best_options += get_auto_complete_list(map_files, substring, new_best_options, score)
            if is_enough(auto_complete_best_options):
                return auto_complete_best_options[:5]
    return auto_complete_best_options[:5]
