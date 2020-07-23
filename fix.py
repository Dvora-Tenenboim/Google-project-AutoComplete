from string import ascii_lowercase

COMPLETIONS_NUM=5

def is_enoughf(set_options):
    return len(set_options)>=COMPLETIONS_NUM

def get_ascii_lowercase_exclude_current_char(char):
    return ascii_lowercase.replace(char,"")


def get_remove_char_options(substring, map_substring, start,end):
    match_values = set()
    for i, char_to_remove in enumerate(substring[start:end], start):
        match_values.update(set(map_substring.get(substring[:i] + substring[i+1:], [])))
        if is_enoughf(match_values):
            return list(match_values)[:5]
    return list(match_values)[:5]

def get_add_char_options(substring, map_substring, start,end):
    match_values = set()
    for i in range(start,end):
        for _char in ascii_lowercase:
            match_values .update(set(map_substring.get(substring[:i] + _char + substring[i:], [])))
            if is_enoughf(match_values):
                return list(match_values)[:5]
    return list(match_values)[:5]

def get_changed_char_options(substring, map_substring, start,end):
    match_values=set()
    end = end + 1 if end != -1 else len(substring)
    for i,char_to_replace in enumerate(substring[start:end],start):
        for char in get_ascii_lowercase_exclude_current_char(char_to_replace):
            match_values.update(set(map_substring.get(substring[:i] + char + substring[i + 1:], [])))
            if is_enoughf(match_values):
                return list(match_values)[:5]
    return list(match_values)[:5]

def get_add_or_remove_char_options(substring, map_substring, start,end):
    match_values = set()
    end = end + 1 if end != -1 else len(substring)
    match_values.update(get_remove_char_options(substring, map_substring, start,end))
    if not is_enoughf(match_values):
        match_values .update(get_add_char_options(substring, map_substring, start, end))
    return list(match_values)[:5]

