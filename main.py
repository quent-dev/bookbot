def main ():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    def count_words():
        words = file_contents.split()
        return len(words)

    def count_characters():
        char_count = {}

        for char in file_contents.lower():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
    

    def report():
        print(f"--- Begin report of {path_to_file} ---\n")
        print(f"{count_words()} words found in the document\n")
        char_count = count_characters()
        for char in char_count:
            if char.isalpha():
                print(f"The '{char}' character was found {char_count[char]} times")
        print("--- End report ---")

    report()

main()
