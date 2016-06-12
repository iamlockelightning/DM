
import os
import word2vec
import pickle

MAX_LEN = 80
VEC_DIM = 100

def transferUsingWord2Vec(max_len=None):
    vec_set = []
    keyworddir = "D:data/keyword/"
    model = word2vec.load('vectors_100.bin')
    for parent,dirnames,filenames in os.walk(rawdir):
        for filename in filenames:
            fr = open(os.path.join(parent,filename), 'r')
            doc = fr.read()
            fr.close()
            keywords = doc.split('|')
            wordvec = []
            for word in keywords:
                if word in model.vocab:    
                    wordvec.append( model[word].tolist() )

            l = len(wordvec)
            if l == 0:
                print 'No Words!!!___' + filename
            else:
                if max_len!=None:
                    for i in range(l, MAX_LEN):
                        wordvec.append( [0]*VEC_DIM )

            vec_set.append( wordvec )

    return vec_set

def getLabel():
    pass

def saveAsPickle(data):
    output = open('data.pkl', 'wb')
    pickle.dump(data, output)
    output.close()

def loadPickle():
    pkl_file = open('data.pkl', 'rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    return data

if __name__=="__main__":
    keyworddir = "D:data/keyword/"
    transferUsingWord2Vec()
    