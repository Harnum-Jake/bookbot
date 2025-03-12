def count_words(book_text):
        word_count = len(book_text.split()) #Use split() to convert book text into a list of words
        print(f"Found {word_count} total words")

def count_characters(book_text):
	book_text_lower = book_text.lower() #lower case all characters
	char_counts = {}
	for char in book_text_lower:
		if not char.isalpha():
			continue
		#If the character already exists in the dictionary add a count
		if char in char_counts:
			char_counts[char] += 1
		#If its not in there yet, make a new key with the associated char and set to 1
		else:
			char_counts[char] = 1
	return char_counts

def sort_char_counts(char_counts):
	sorted_chars = []
	for char,count in char_counts.items():
		sorted_chars.append({"character": char, "count": count})

	for i in range(len(sorted_chars)):
		for j in range(i + 1,len(sorted_chars)):
			if sorted_chars[i]["count"] < sorted_chars[j]["count"]:
				#Sorting time
				sorted_chars[i], sorted_chars[j] = sorted_chars[j], sorted_chars[i]
	return sorted_chars
