def total_words(text):
    # split the text into a list of individual words, breaking on whitespace
    words = text.split()
    # count how many words are in that list
    return len(words)


def get_num_chars(chars):
    # dictionary to store character -> count pairs
    book_count = {}
    # loop through the text one character at a time
    for letter in chars:
        # normalize to lowercase so 'A' and 'a' count as the same character
        lower_case = letter.lower()
        if lower_case in book_count:
            # character already seen, increment its count
            book_count[lower_case] = book_count[lower_case] + 1
        else:
            # first time seeing this character, start its count at 1
            book_count[lower_case] = 1
    # return the finished dictionary of character counts
    return book_count


def sort_on(value):
    # accepts a tuple like ("b", 4868)
    # returns the count value (index 1), used by sorted() to compare tuples
    return value[1]


def chars_dict_to_sorted_list(chars_count):
    # list that will hold (character, count) tuples
    list_keys = []
    # loop over each character (key) in the dictionary
    for key in chars_count:
        # look up how many times this character appeared
        count = chars_count[key]
        # bundle the character and its count into a tuple
        char_tuple = (key, count)
        # add the tuple to our list
        list_keys.append(char_tuple)

    # sort the list from highest count to lowest,
    # using sort_on to tell sorted() to compare by count instead of character
    sorted_counts = sorted(list_keys, reverse=True, key=sort_on)
    # return the sorted list of tuples
    return sorted_counts





