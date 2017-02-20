# -*- coding: utf-8 -*-
import logging
import json
from gensim import corpora, models, similarities

class Recomendation(object):
    def main(self):
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

        dictionary = corpora.Dictionary.load('chatbot.dict')
        corpus = corpora.MmCorpus('chatbot.mm')
        lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

        doc = raw_input("Enter something: ")
        print ("you entered " + doc)
        doc = doc.decode('utf-8')

        vec_bow = dictionary.doc2bow(doc.lower().split())
        vec_lsi = lsi[vec_bow]
        index = similarities.MatrixSimilarity(lsi[corpus])
        index.save('chatbot.index')
        index = similarities.MatrixSimilarity.load('chatbot.index')
        sims = index[vec_lsi]

        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        print(sims[:10])
        index = []
        for result in sims:
            data = list(result)
            if data[1] > 0.99:
                index.append(data[0])

        if len(index) == 0:
            print("no result matching.........")
        else:
            with open('data.json') as data_file:
                datas = json.load(data_file)

            if len(index) > 10:
                index = index[:10]
            else:
                index
            print index
            # index = [[data[1] data = list[result] if data[1] > 1]for result in sims]

            for i in index:
                print datas[i]



if __name__ == "__main__":
    Recomendation().main()