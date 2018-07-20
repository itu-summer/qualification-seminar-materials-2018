import string


class TextAnalysis():
	def __init__(self):
		""" Gets all leters and punctuations from string module."""
		self.letters = string.ascii_letters
		self.punctuation = string.punctuation


	def read_file(self, file):
		""" All functions uses this read function to read in the file."""
		with open(file) as f:
			text = f.read()
		return text


	def count_paragraphs(self, file):
		""" Counts number of pragraphs."""
		text = self.read_file(file)
		text = text.split("\n\n")
		return len(text)


	def count_words(self, file):
		""" Counts number of words."""
		text = self.read_file(file)
		text = text.replace("\n", " ")
		text = text.split(" ")
		count = 0
		for element in text:
			if len(element) != 0:
				count += 1
		return count


	def count_char(self,file):
		""" Counts number of characters."""
		text = self.read_file(file)
		count = 0
		text = text.replace("\n","")
		for char in text:
			if char in self.letters:
				count += 1
		return count


	def remove_punctuation(self, file):
		""" Remove punctuation by replacement."""
		text = self.read_file(file)
		for char in text:
			if char in self.punctuation:
				text = text.replace(char, "")
		return text


if __name__ == '__main__':
	""" Example of use."""
	TA = TextAnalysis()
	file = "./a_study_in_scarlet.txt"
	print(TA.count_paragraphs(file))
	print(TA.count_words(file))
	print(TA.count_char(file))
	print(TA.remove_punctuation(file))
