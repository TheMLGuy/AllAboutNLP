from nltk.stem import PorterStemmer
from nltk.tokenizer import word_tokenizer
#Stemmer can be used to stem each word to its root
#example consider pythonly, pythoning, pythoner, pythoned, pythoning- common root is python, so stemming when applied
#to these words will reduce each word to its root
stemmer=PorterStemmer()
example_sentences="Hi I am Ashwin and am passionate about machine learning and domain of predictive analytics"

words=word_tokenizer(example_sentences)

for w in words:
	print(stemmer.stem(w))
	
'''
Hi
I
am
ashwin
and
am
passion
about
machin
learn
and
domain
of
predict
analyt
'''	