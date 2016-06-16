# -*- coding:utf-8 -*- 

import os
import re
from collections import Counter
from nltk.corpus import stopwords

def extractWord(rawdir):
    
    STOP_WORDS = []

    count = 0
    print "load file..."
    for parent,dirnames,filenames in os.walk(rawdir):
        for filename in filenames:
            count += 1
            if count%1000 == 0:
                print count

            fr = open(os.path.join(parent,filename), 'r')
            doc = fr.read()
            fr.close()

            text = doc[1:-2]

            line = re.sub('[^A-Za-z]', ' ', text)
            word_list = re.sub('[\s]+', ' ', line).lstrip().rstrip().split(' ')
            filtered_word_list = word_list[:]
            for word in word_list:
                if (word in stopwords.words('english')) or word in STOP_WORDS: 
                    filtered_word_list.remove(word)

            words_str = ''
            for w in filtered_word_list:
                words_str += w + ' '
            
            wr = open(os.path.join(parent,filename+'.words'), 'w')
            wr.write( words_str.rstrip() )
            wr.close()

def wordFilter(rawdir):
    
    NEW_STOP_WORDS = []

    print "load file..."
    for parent,dirnames,filenames in os.walk(rawdir):
        for filename in filenames:
            if os.path.splitext(filename)[1][0:]=='.words':
                fr = open(os.path.join(parent,filename), 'r')
                doc = fr.read()
                fr.close()
                word_list = doc.split(' ')
                filtered_word_list = word_list[:]
                for word in word_list:
                    if word in NEW_STOP_WORDS: 
                        filtered_word_list.remove(word)

                words_str = ''
                for w in filtered_word_list:
                    words_str += w + ' '

                wr = open(os.path.join(parent,filename), 'w')
                wr.write( words_str.rstrip() )
                wr.close()

label_dict = {}
def readLabel(dirr="classifier.txt"):
    print "load label..."
    rf = open(dirr, 'r')
    # val_dict = {}
    for line in rf:
        line = line[0:-1].split('>')
        vallist = line[1].split(' ')
        val = 0
        base = 1
        for i in range(len(vallist)):
            if vallist[len(vallist)-1-i]=='0':
                base *= 2
            elif vallist[len(vallist)-1-i]=='1':
                val += base
                base *= 2

        label_dict[ line[0][1:-1] ] = val
        # val_dict[ val ] = val
    # print len(sorted(val_dict))
    rf.close()


def makeData(rawdir):
    print "load file..."
    word_dict_key = []
    text_dict = {}
    for parent,dirnames,filenames in os.walk(rawdir):
        for filename in filenames:
            if os.path.splitext(filename)[1][0:]=='.words':
                fr = open(os.path.join(parent,filename), 'r')
                doc = fr.read()
                fr.close()
                word_list = doc.split(' ')

                text_dict[ filename.split('.')[0]+'.txt' ] = Counter(word_list)
                word_dict_key.extend( Counter(word_list).keys() )

    word_dict_key = list(set(word_dict_key))

    count = 0
    print 'write out...'
    wo = open('dataSVM.txt', 'w')
    for key,val in text_dict.items():
        count += 1
        if count%1000 == 0:
            print count

        wo.write(str(label_dict[ key ]) + ' ')
        index_dict = {}
        for w in val.keys():
            index_dict[ w ] = word_dict_key.index(w)

        index_dict = sorted(index_dict.items(), lambda x, y: cmp(x[1], y[1]))
        # print index_dict
        for i in index_dict:
            wo.write(str( i[1] ) + ':' + str( val[ i[0] ] ) + ' ')

        wo.write('\n')

    wo.close()

if __name__=="__main__":

    rawdir = "C:/Users/locke/Desktop/doc"
    dirr="classifier.txt"
    
    # extractWord(rawdir)
    
    wordFilter(rawdir)

    
    readLabel(dirr)

    makeData(rawdir)
