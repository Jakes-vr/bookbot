def get_num_words(text):
        words = text.split()
        return len(words)

def char_count(text):
	count = {}
	for char in text:
		lowercase_char = char.lower()
		if lowercase_char in count:
			count[lowercase_char] += 1
		else:
			count[lowercase_char] = 1
	return count
