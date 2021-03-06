# logging
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


from gensim import corpora, models, similarities

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]


# remove common words and tokenize
stoplist = set('for a of the and to in'.split())

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)

texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
for text in texts:
	for token in text:
		frequency[token] += 1
texts = [[token for token in text if frequency[token] > 1] for text in texts]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

print(dictionary.token2id)
print corpus


