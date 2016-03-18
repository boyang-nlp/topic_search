#coding=utf-8
import jieba
import pickle
import conf
from gensim import corpora

def build_corpus():
	fdic = conf.dictionary
	cache = conf.cache
	fin = open(conf.raw_post, 'r')
	fout = open(conf.corpus, 'wb+')
	posts = []
	text = ''
	dic = corpora.Dictionary()
	while True:
		line  = fin.readline()
		if line == '':
			break
		if line[0:3] != conf.eop[0:3]:
			text += line
			continue
		bow = dic.doc2bow(list(jieba.cut(text)), allow_update = True)
		text = ''
		if len(posts) < cache:
			posts.append(bow)
		else:
			objs = bytearray()
			for obj in posts:
				objs += pickle.dumps(obj)
			fout.write(objs)
			posts = []
	if len(posts) != 0:
		objs = bytearray()
		for obj in posts:
			objs += pickle.dumps(obj)
		fout.write(objs)
	dic.save(fdic)
	fin.close()
	fout.close()

def load_corpus():
	f = open(conf.corpus, 'rb')
	corpus = []
	while True:
		try:
			s = pickle.load(f)
		except EOFError:
			break
		else:
			corpus.append(s)
	f.close()			
	return corpus