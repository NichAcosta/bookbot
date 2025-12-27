def main():
    import sys
    from stats import count_words
    from stats import character_count
    from stats import sort_list
    try:
        path = sys.argv[1]
    except IndexError as e:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(path)
    word_count = count_words(book)
    alphabet_count = character_count(book)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}...")
    print ("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print ("--------- Character Count -------")
    sort_list(alphabet_count)
    print ("============= END ===============")
    
def get_book_text (file):
    with open(file) as contents:
        return contents.read()

main()
    
    
