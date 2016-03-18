#coding=utf-8
import corpus
import lda
import search
from gensim import corpora, models
"""
corpus.build_corpus()
c = corpus.load_corpus()
print 'Hello'
for i in c:
	print i
lda.init_tfidf()
lda.train_lda()
post = lda.load_topic_of_post()
for p in post:
	print p
"""
h = search.query(u'女歌手')
for i in h:
	print i[0]
	print i[1]