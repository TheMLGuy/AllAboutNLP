import nltk
import random
from nltk.corpus import movie_reviews

print(movie_reviews.categories())
# ['pos','neg']

docs=[(list(movie_reviews.words(fileid)), category)
		for category in movie_reviews.categories()
		for fileid in movie_reviews.fileids(category)	]

random.shuffle(docs)		

all_words=[]
for w in movie_reviews.words():
	all_words.append(w)
all_words=nltk.FreqDist(all_words)

print(all_words("gorgeous"))
#50