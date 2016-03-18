#coding=utf-8
import pickle
import corpus
import conf
import jieba
import numpy as np
import heapq
from gensim import corpora, models
from lda import load_topic_of_post

def get_post(sel):
	f = open(conf.raw_post, 'r')
	idx = 0
	text = ''
	while True:
		line  = f.readline()
		if line == '':
			break
		if line[0:3] != conf.eop[0:3]:
			text += line
			continue
		if idx in sel.keys():
			sel[idx] = (sel[idx], text)
		text = ''
		idx += 1
	return sel

def query(sentence, result = 3):
	dic = corpora.Dictionary.load(conf.dictionary)
	tfidf = models.TfidfModel.load(conf.tfidf)
	lda = models.LdaModel.load(conf.lda)
	q_topic = lda[tfidf[dic.doc2bow(jieba.lcut_for_search(sentence))]]
	topics = load_topic_of_post()
	martix = np.zeros((len(topics), conf.num_topics), float)
	for ti, t in enumerate(topics):
		for tj,v in t:
			martix[ti,tj] = v
	q_vec = np.zeros(conf.num_topics, float)
	for ti,v in q_topic:
		q_vec[ti] = v
	pq = []
	i = 0
	while i < len(topics):
		heapq.heappush(pq, (sum((martix[i] - q_vec)**2), i))
		i+=1
	sel = {}
	for s, i in heapq.nsmallest(result, pq):
		sel[i] = s
	print sel
	post = get_post(sel).values()
	post.sort()
	return post






