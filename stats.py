def get_word_count(text):
    words = text.split()
    return len(words) 

def get_char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# python
def sort_on(item):
    return item["num"]

def sort_char_count(char_count):
    list_of_dicts = [{"char": k, "num": v} for k, v in char_count.items()]
    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts

