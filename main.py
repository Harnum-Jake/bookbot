from stats import count_words,count_characters,sort_char_counts
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	file_location = sys.argv[1]
	try: #Get the book text from the user
		book_text = get_book_text(file_location)
		characters = count_characters(book_text)
		sorted_char_list = sort_char_counts(characters)
		print("============ BOOK BOT ============")
		print(f"Analyzing book found at {file_location}...")
		print("----------- Word Count ----------")
		count_words(book_text)
		print("--------- Character Count -------")
		for entry in sorted_char_list:
			print(f"{entry['character']}: {entry['count']}")
		print("============= END ===============") 
	except FileNotFoundError:
		print(f"Error: The requested file '{file_location}' was not found.")
		sys.exit(1)
main()
