#coding=utf-8
import conf
import pickle
import corpus
from gensim import corpora, models

def init_tfidf():
	tfidf = models.TfidfModel(corpus.load_corpus())
	tfidf.save(conf.tfidf)
	return tfidf
	
def train_lda():
	tfidf = models.TfidfModel.load(conf.tfidf)
	corpus_tfidf = tfidf[corpus.load_corpus()]
	lda = models.LdaModel(corpus_tfidf, id2word=corpora.Dictionary.load(conf.dictionary), num_topics=conf.num_topics)
	corpus_topics = lda[corpus_tfidf]
	objs = bytearray()
	for obj in corpus_topics:
		objs += pickle.dumps(obj)
	f = open(conf.corpus_topics, 'wb')
	f.write(objs)
	f.close()
	lda.save(conf.lda)
	return lda

def load_topic_of_post():
	f = open(conf.corpus_topics, 'rb')
	post = []
	while True:
		try:
			s = pickle.load(f)
		except EOFError:
			break
		else:
			post.append(s)
	return post