def count_words(text):
    lst_words = text.split()
    return len(lst_words)


def count_characters(text):
    char_count_dict = {}
    for char in text:
        if char.lower() not in char_count_dict:
            char_count_dict[char.lower()] = 1
        else:
            char_count_dict[char.lower()] += 1

    return char_count_dict


def sort_on(dict):
    for key in dict:
        return dict[key]


def sort_char_dict(char_dict):
    sort_list = []
    for key in char_dict:
        if key.isalpha():
            sort_list.append({key: char_dict[key]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
