from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_sentence="Hi I am Ashwin and am passionate about machine learning and domain of predictive analytics"
stopwords=set(stopwords.words("english"))
#stopwords are words of the type "are", "is","or" which when removed will still retain the meaning of the paragraph
return [w for w in word_tokenize(example_sentence) if w not in stopwords]
'''['Hi',
 'I',
 'Ashwin',
 ',',
 'data',
 'sleuth',
 ';',
 'building',
 'career',
 'predictive',
 'analytics']'''