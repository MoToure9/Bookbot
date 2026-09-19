import sys
from stats import total_words
from stats import get_num_chars
from stats import chars_dict_to_sorted_list

def get_book_text(text):
    with open(text) as f:
        text_contents = f.read()
    return text_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count = total_words(text)
    
    
    character_counts = get_num_chars(text)
    sorted_counts = chars_dict_to_sorted_list(character_counts)
    print_report(book_path, count, sorted_counts)
    


def print_report(book_path, count, sorted_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char, char_count in sorted_counts:
        if not char.isalpha():
            continue
        print(f"{char}: {char_count}")
    print("============= END ===============")


        
 
    






main()









