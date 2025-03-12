def get_num_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_char_counts(char_counts):
    sorted_list=[{"char": char, "count": count} for char,count in char_counts.items()]
    sorted_list.sort(key=lambda item: item['count'], reverse=True)
    return sorted_list