
# Experminetal code for boot.dev
from stats import *
import sys


def get_book_text(path):
    with open(path) as f:
        txt = f.read()
        f.close()
    return txt

def main():
    warn_txt = """Usage: python3 main.py <path_to_book>"""

    if len(sys.argv) != 2:
        print(warn_txt)
        sys.exit(1) # This is important!!!
    else:
        # This is horribly optimized...
        path = sys.argv[1] # easy
        txt = get_book_text(path)
        
        # print(get_book_text(path)) # Easy...
        
        # Standard stat tools
        num_words = count_words(get_book_text(path))
        letter_counts = count_letters(txt)
        sd = sort_dict(letter_counts)
    
        
        # Report elements...
        # A lot of print statements in series...
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for l in sd:
            # I'm sure there's a better way to handle the dictionary variables...
            c = l["char"]
            n = l["num"]
            print(f"{c}: {n}")
        print("============= END ===============")

main()