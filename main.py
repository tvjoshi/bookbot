from pathlib import Path
import sys
from typing import Union
from stats import get_num_words, get_char_counts

def get_book_text(file_path: Union[str, Path]) -> str:
	"""Return the contents of file_path as a string."""
	path = Path(file_path)
	if not path.is_file():
		raise FileNotFoundError(f"File not found: {path}")
	return path.read_text(encoding="utf-8")

def main(book_path_arg: str) -> None:
	"""Analyze the book at book_path_arg for word and character counts."""
	# Resolve provided path (relative paths are relative to project root)
	book_path = Path(book_path_arg)
	if not book_path.is_absolute():
		book_path = Path(__file__).resolve().parent / book_path

	try:
		text = get_book_text(book_path)
	except Exception as e:
		print(f"Error reading book: {e}", file=sys.stderr)
		sys.exit(1)

	# Print header and show relative path to the book file
	try:
		rel_path = book_path.relative_to(Path(__file__).resolve().parent)
	except Exception:
		rel_path = book_path
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {rel_path}...")
	print("----------- Word Count ----------")
	num_words = get_num_words(text)
	print(f"Found {num_words} total words")
	# Character count header
	print("--------- Character Count -------")
	# Print dictionary of character counts (lowercased), only alphabetical chars, sorted desc by count
	char_counts = get_char_counts(text)
	for c, count in sorted(char_counts.items(), key=lambda kv: kv[1], reverse=True):
		# skip non-alphabetical characters
		if not c.isalpha():
			continue
		print(f"{c}: {count}")

if __name__ == "__main__":
	# Require exactly one CLI argument (script name + path)
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	main(sys.argv[1])