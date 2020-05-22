import gensim
import jieba
import numpy as np
from scipy.linalg import norm
from gensim.models import word2vec
import os



root = 'E:/LawNLP/文书'
root2 = 'E:/LawNLP/data'
input_path = root2 + '/938/刑事案件'
compare_files = []
input_files = []
file1s = os.listdir(input_path)
file2s = os.listdir(root)
for file1 in file1s:
    if os.path.isdir(input_path):
        input_files.append(input_path + '/' + file1)
for file2 in file2s:
    compare_path = root + '/' + file2 + '/刑事案件'
    if os.path.isdir(compare_path):
        files = os.listdir(compare_path)
        for file in files:
            compare_files.append(compare_path + '/' + file)


model = word2vec.Word2Vec.load('lawModel_2.word2vec')


def initial():
    stopwords_file = "E:\\LawNLP\\stopword.txt"

    stop_f = open(stopwords_file,"r",encoding='utf-8')
    stop_words = list()
    for line in stop_f.readlines():
        line = line.strip()
        if not len(line):
            continue

        stop_words.append(line)
    stop_f.close
    return stop_words


def segmentation(path):
    stop = initial()
    file = open(path,"r",encoding='utf-8')
    compare_list = list()
    for line in file.readlines():
        line = line.strip()
        if not len(line):
            continue
        outstr = ''
        seg_list = jieba.cut(line)
        for word in seg_list:
            if model.wv.__contains__(word):
                compare_list.append(word)
    file.close
    return compare_list


def compute_similarity(f1, f2):

    for filename1 in f1:
        max = -1
        for filename2 in f2:
            result = model.wv.n_similarity(segmentation(filename1), segmentation(filename2))
            if result > max:
                max = result
                most_similar_file = filename2
        print('Input File' + filename1)
        print('Output File' + most_similar_file)
        print(max)


compute_similarity(input_files, compare_files)
