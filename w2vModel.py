# -*- coding: utf-8 -*-
import warnings

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import word2vec
import logging

# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"path")  # 加载语料
n_dim = 1000
# 训练skip-gram模型;
model = word2vec.Word2Vec(sentences, size=n_dim, min_count=5, sg=1)
# 训练CBOW模型
model = word2vec.Word2Vec(sentences, size=n_dim, min_count=5, sg=0)
model.save('lawModel_2.word2vec')

y = model.wv.most_similar("测试单词",topn=10)
for item in y:
    print(item[0],item[1])
