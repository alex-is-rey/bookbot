import sys
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    word_count = get_word_count(file_contents)
    char_count = get_char_count(file_contents)
    sorted_char_count = sort_char_count(char_count)  
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ---------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count[:]:
        if item['char'].isalpha():  # Only print alphabetic characters
            print(item['char'] + ":", item['num'])
        else:
            continue
    print("============= END ===============")    
   
from stats import get_word_count 
from stats import get_char_count    
from stats import sort_char_count
main()
