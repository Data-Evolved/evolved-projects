

# Common Definitions

**part-of-speech POS**


# Text Normalization 

Stemming is quicker and more coarse grain while lemmatization provides contextual intelligence in reducing the word. 

**stemming** a text normalization technique that cuts off the end or beginning of word by looking for common prefixes and suffixes (e.g. "ly") and stripping them. 

NLTK: `PorterStemmer`
spaCy: `None`

**lemmatization** a text normalization technique that attempts to obtain the root form of a word, the lemma.

NLTK: `WordNetLemmatizer`
spaCy: `en_core_web_sm` library 


# Stopwords

**stopwords** are the most commmon words in any natural language in which might not have much value or meaning when analyzing text and documents. This does not mean we should remove them for all NLP tasks. 

NLTK has stopwords in 16 different languages. 

spaCy has its own stopwords.

gensim can remove stopwords without tokenization. 


