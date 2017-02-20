from textblob.classifiers import NaiveBayesClassifier

with open('training.csv', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="csv")

a = cl.classify("apple iphone 7")
print(a)