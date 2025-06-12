def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	content  = get_book_text("/home/jaco/workspace/github.com/jakes-vr/bookbot/books/frankenstein.txt")
	print(content)

main()
