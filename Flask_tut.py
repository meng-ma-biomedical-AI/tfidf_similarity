import string
from sklearn.feature_extraction.text import TfidfVectorizer
from difflib import SequenceMatcher
import csv
import gensim
import nltk
from gensim import corpora, models, similarities
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
#reading csv file
f = csv.reader(open('C:\\Users\\vedan\\Downloads\\medcondition.csv', 'r'))

#function to calculate similarity

def similar(alpha1, alpha2):
    corpus = [alpha1, alpha2]
    vect = TfidfVectorizer(min_df=1, stop_words="english")
    tfidf = vect.fit_transform(corpus)
    pairwise_similarity = tfidf * tfidf.T
    pairwise_similarity = pairwise_similarity.toarray()
    pairwise_similarity = pd.DataFrame(pairwise_similarity)
    #returns the ratio
    return pairwise_similarity[0][1]


#dictionary to story csv doc
d = {}

#THE FILE IS OF THE FORM:ID, DESCRIPTION, PROBLEM. SO id-->wgt, des-->description, p-->problem
# where wgt serves as the key and des,p serve as values
def add_d(wgt, des, p):
    d[wgt] = (des, p)


count = 0
num = 0


#reading each row/line in f
for row in f:
    w = row[0]  # weight
    k = row[1]  # description
    v = row[2]  #problem
    add_d(w, k, v) # adds these values to the dictionary d


for x, (y, z) in d.items():
    str1 = y
    s1 = z
    c1 = y+z
    for a, (b, c) in d.items():
        str2 = b
        s2 = c
        c2 = b+c
        #sim = similar(str1, str2)#calls the function similar
        #sim2 = similar(s1,s2)
        sim3 = similar(c1,c2)
        print(sim3)

        count = count + 1
        if sim > 0.09:
            num =num + 1
            if c == "vdv":      #vdv is the problem. suppopse we have 4 similar descrpitions be we want to find only those whose problem is of the kind'vdv'
                print(a)
                print(c)
print(num)
print(count)
