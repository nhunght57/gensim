import logging
import json
import codecs
from gensim import corpora, models, similarities
from collections import defaultdict
from pprint import pprint

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


documents = []

with open('data.json') as data_file:
    datas = json.load(data_file)
    for data in datas:
        documents.append(data['title'
                              ''])

# pprint(documents[29])

with codecs.open('stoplist.txt', encoding='utf-8') as f:
    for line in f:
        stoplist = set(line.lower().split())

# pprint(stoplist)

texts = [[word for word in document.lower().split() if word not in stoplist]for document in documents]

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
texts = [[token for token in text if frequency[token] > 1]for text in texts]

# i = 901
# while  i < 937:
#     pprint(texts[i])
#     i = i+1

dictionary = corpora.Dictionary(texts)

dictionary.save('chatbot.dict')

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('chatbot.mm', corpus)
# print(corpus)
