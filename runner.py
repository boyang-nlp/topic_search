#coding=utf-8
import corpus
import lda
import search
import conf
def do_query():
	while True:
		sen = raw_input(u'Start Query Here->:')
		result = search.query(sen)
		for item in result:
			print 'similarity : {0} \n {1}'.format(item[0], item[1])

def build():
	f = open(conf.init, 'r+')
	inited = f.readline()
	if inited == conf.uninitialized:
		print 'build topic model...'
		corpus.build_corpus()
		lda.init_tfidf()
		lda.train_lda()
		f.write(conf.initialized)
	else:
		print 'topic model has been build'
	f.close()


#main
build()
do_query() 
