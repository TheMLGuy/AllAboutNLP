from nltk.corpus import state_union
from nltk.tokenize import word_tokenize, sent_tokenize

train_text=state_union.raw('2005-GWBush.txt')
test_text=state_union.raw('2006-GWBush.txt')

sentences=sent_tokenize(train_text)
for i in sentences:
	words=word_tokenize(i)
	tagged=nltk.pos_tag(words)
	#chink is all about exclude content from chunked data
	chunkgram=r"""Grouping:{<RB.?>*<VB.?>*<NNP>+<NN>?} }<VB.?|IN|DT>{ """
	chunkParser=nltk.regexpParser(chunkgram)
	chunked=chunkParser.parse(tagged)
	
	
