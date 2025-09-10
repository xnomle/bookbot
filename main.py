import sys
from requests import get
from stats import count_word, each_char, sorted_dict

def get_book_text(path):
    with open(path) as b: 
        text = b.read()
    return text      

def main():
    print("Usage: python3 main.py <path_to_book>")
    path = sys.argv[1]
    if path == False:
        sys.exit(1)
    content = get_book_text(path) 
    num_words =count_word(content)
    char_count = each_char(content)
    sort = sorted_dict(char_count)
    print(f"============ BOOKBOT ============\nAnalyzing book found at{path}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count ------- ")
    for a in sort:
       print(f"{a['char']}: {a['num']}")
            
        
          

main()    

