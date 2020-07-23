from auto_complete_data import AutoCompleteData
from completion import get_best_k_completions
from init import clean

STOP_INPUT = "#"
STOP_PROGRAM = "exit"


def run(map_substring, map_files):
    while True:
        user_input = input("Enter your text\n")
        if user_input == STOP_PROGRAM:
            break
        while True:
            if user_input[-1] == STOP_INPUT:
                break
            auto_complete_best_options = get_best_k_completions(clean(user_input), map_substring, map_files)
            if not auto_complete_best_options:
                print(f"no suggestions for {user_input}")
                break
            for i, auto_complete_option in enumerate(auto_complete_best_options, 1):
                print(f"{i}:{auto_complete_option}")
            user_input += input(user_input)
