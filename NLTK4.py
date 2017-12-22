from nltk.corpus import state_union
#state_union 
from nltk.tokenize import word_tokenize
sample_sentence="Hi I am Ashwin and am passionate about machine learning and domain of predictive analytics"
tokenized=word_tokenize(sample_sentence)
#pos_tag The process of classifying words according to their parts of speech is
# handled via nltk.pos_tag()

words_with_pos=nltk.pos_tag(tokenized)
print(words_with_pos)

'''
[('Hi', 'NNP'), ('I', 'PRP'), ('am', 'VBP'), ('Ashwin', 'NNP'), 
('and', 'CC'), ('am', 'VBP'), ('passionate', 'VB'), ('about', 'IN'),
 ('machine', 'NN'), ('learning', 'NN'), ('and', 'CC'), ('domain', 'NN'),
 ('of', 'IN'), ('predictive', 'JJ'), ('analytics', 'NNS')]
'''

#There may be cases when the same word can appear as a noun and a verb as well, so it is important
#to understand how parts of speech for the given text. This is required to handle homonyms.