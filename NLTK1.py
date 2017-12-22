from nltk.tokenize import sent_tokenize, word_tokenize
# how does tokenize work?

#can use sent_tokenize to tokenize sentences
#input:paragraph
#output:sentences


#word_tokenize outputs all words in a paragraph
example_text="Hi I am Ashwin, a data sleuth; building a career in predictive analytics"
print(sent_tokenize(example_text))
# ['Hi I am Ashwin, a data sleuth; building a career in predictive analytics'] is the ouput
print(word_tokenize(example_text))
'''['Hi',
 'I',
 'am',
 'Ashwin',
 ',',
 'a',
 'data',
 'sleuth',
 ';',
 'building',
 'a',
 'career',
 'in',
 'predictive',
 'analytics']'''