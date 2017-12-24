#Lemmatizing is similar to stemming, except the end result will be a real word
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

print(lemmatizer.lemmatize("runner"))
#runner
print(lemmatizer.lemmatize("runner",'a'))
#runner
print(lemmatizer.lemmatize("better"))
#better
print(lemmatizer.lemmatize("better",'a'))
#good
#difference between porterstemmer and wordnetlemmatizer
sent = "cats running ran cactus cactuses cacti community communities"
from nltk.stem import PorterStemmer, WordNetLemmatizer

port = PorterStemmer()
" ".join([port.stem(i) for i in sent.split()])
#'cat run ran cactu cactus cacti commun commun'

wnl = WordNetLemmatizer()
" ".join([wnl.lemmatize(i) for i in sent.split()])
#'cat running ran cactus cactus cactus community community'
