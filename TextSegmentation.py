#encoding = utf-8
import jieba
import re
import glob
import os
jieba.enable_paddle()



def initial(path):
    stopwords_file = path

    stop_f = open(stopwords_file,"r",encoding='utf-8')
    stop_words = list()
    for line in stop_f.readlines():
        line = line.strip()
        if not len(line):
            continue

        stop_words.append(line)
    stop_f.close
    return stop_words


path2 = "E:\\LawNLP\\textSegmentation.txt"

result = list()

root = 'E:/LawNLP/文书'
compare_files = []
file2s = os.listdir(root)
for file2 in file2s:
    compare_path = root + '/' + file2 + '/刑事案件'
    if os.path.isdir(compare_path):
        files = os.listdir(compare_path)
        for file in files:
            compare_files.append(compare_path + '/' + file)

for filename in compare_files:
    f1 = open(filename, encoding='utf-8')
    stop = initial()
    for line in f1.readlines():
        line = line.strip()
        if not len(line):
            continue
        outstr = ''
        seg_list = jieba.cut(line,cut_all=False)
        for word in seg_list:
            if word not in stop:
                if word != '\t':
                    if word != " ":
                        result.append(word)
    f1.close()

#print(result)
f2 = open(path2, 'w', encoding='utf-8')
for word in result:
    f2.write(word + " ")
f2.close()