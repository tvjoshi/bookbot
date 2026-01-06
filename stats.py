def get_num_words(text: str) -> int:
	"""Return the number of words in text (splits on whitespace)."""
	return len(text.split())

def get_char_counts(text: str) -> dict[str, int]:
	"""Return a dict mapping each unique character (lowercased) to its count in text."""
	counts: dict[str, int] = {}
	for ch in text.lower():
		counts[ch] = counts.get(ch, 0) + 1
	return counts
