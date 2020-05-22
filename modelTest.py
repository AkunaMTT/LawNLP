from gensim.models import word2vec

model = word2vec.Word2Vec.load('lawModel.word2vec')


word = '金马'
if model.wv.__contains__(word):
    print(1)
else:
    print(0)