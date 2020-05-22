# LawNLP
A tiny program to compute the similarity of two judicial documents and recommend the most similar one of the input doucument
## What's in this
textsegemtation uses jieba to do the text segmentation in Chinese and add them to the corpus  
w2vModel is the training program,skip-gram and cbow are both used when training  
SimilarityCompute.py is to compute the similarty between two document and recommend the most similar file then print their similarity
