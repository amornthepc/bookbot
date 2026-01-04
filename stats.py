def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_num(text):
    char_nums = {}
    text = text.lower()
    for c in text:
        if c not in char_nums:
            char_nums[c] = 1
            continue
        char_nums[c] += 1

    return char_nums

def sort_on(items):
    return items["num"]

def sort_dict_list(char_dict):
    dict_list = []
    for k in char_dict:
        tmp_dict = {}
        tmp_dict["char"] = k
        tmp_dict["num"] = char_dict[k]
        dict_list.append(tmp_dict)

    dict_list.sort(reverse=True, key=sort_on) 
    return dict_list
