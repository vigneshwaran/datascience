
# coding: utf-8

# Importing python library for handling pdf file

import PyPDF2 as pdf
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words=stopwords.words('english')
from collections import Counter


# opening the file in binary form


file=open('JavaBasics-notes.pdf','rb')

# Reading the pdf file

fileobj = pdf.PdfFileReader(file)

no=fileobj.numPages

tokens=[]
for i in range(no):
    pageobj = fileobj.getPage(i)
    text= pageobj.extractText()
    word_tokens=word_tokenize(text)
    punct=['\',','\"','\'\'','``','.',',','!','(',')',';',':','[',']','{','/','//','}','=',',','<','>']
    tokens+=[j for j in word_tokens if j not in punct and stop_words]


tags=nltk.pos_tag(tokens)
nouns=[word for word,tag in tags if tag[:2]=='NN']


from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
noun=[lemmatizer.lemmatize(i) for i in nouns]

count =Counter(noun)
print(count.most_common)
