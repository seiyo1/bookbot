def get_num_words(text):
    word_list = text.split()
    return len(word_list)


def get_num_chars(text):
    counts = {}
    word_list = text.split()
    for word in word_list:
        for char in word.lower():
            if char.isalpha(): 
                counts[char] = counts.get(char, 0) + 1
    return counts


def num_chars_to_sorted_list(counts):
    sorted_list = []
    for key, value in counts.items():
        sorted_list.append({"char" : key, "num": value})
    def sort_on(dict):
        return dict["num"]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    