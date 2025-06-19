def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	content  = get_book_text("/home/jaco/workspace/github.com/jakes-vr/bookbot/books/frankenstein.txt")
	print(content)

from stats import get_num_words, char_count

book_text = get_book_text("/home/jaco/workspace/github.com/jakes-vr/bookbot/books/frankenstein.txt")

num_words = get_num_words(book_text)
print(f"{num_words} words found in the document")

character_count = char_count(book_text)
print(character_count)
