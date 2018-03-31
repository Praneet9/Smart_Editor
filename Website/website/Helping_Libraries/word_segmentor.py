import re
import wordsegment
from collections import Counter

wordsegment.load()

def load_word_segmentor(data_path):
	with open(data_path, 'r', encoding='utf-8') as f:
		text = f.read()


	def tokenize(text):
		pattern = re.compile('[a-zA-Z]+')
		return (match.group(0) for match in pattern.finditer(text.lower())) 
	#if your input is all in lower case other wise remove lower() as in text file some word are Unique



	wordsegment.UNIGRAMS.clear()
	wordsegment.UNIGRAMS.update(Counter(tokenize(text)))

	def pairs(iterable):
		iterator = iter(iterable)
		values = [next(iterator)]
		for value in iterator:
			values.append(value)
			yield ' '.join(values)
			del values[0]

	wordsegment.BIGRAMS.clear()
	wordsegment.BIGRAMS.update(Counter(pairs(tokenize(text))))

	from wordsegment import _segmenter

	def identity(value):
		return value
		
	_segmenter.clean = identity
	#Below statement is needed when results are poor and corpus is large
	_segmenter.total = float(sum(wordsegment.UNIGRAMS.values()))

	return wordsegment
