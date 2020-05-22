import collections
#coding=utf-8

filename = "E:\\LawNLP\\textSegmentation_2.txt"
with open (filename,'rb') as f:
    words_box=[]
    words_box2=[]
    for line in f:
        line.decode("utf-8")
        words_box.extend(line.strip().split())
    for word in words_box:
        word2 = word.decode("utf-8")
        words_box2.append(word2)
print("词的总数为：%s"%len(words_box2))
print("词频结果：%s"%collections.Counter(words_box2))
