
import os
import word2vec
import pickle

MAX_LEN = 42
VEC_DIM = 100

def transferUsingWord2Vec(rawdir="C:/Users/locke/Desktop/key", max_len=MAX_LEN): #41
    vec_set = []
    model = word2vec.load('vectors_100.bin')
    maxlen = -1
    count = 0
    for parent,dirnames,filenames in os.walk(rawdir):
        for filename in filenames:
            count += 1
            if count%1000==0:
                print count

            fr = open(os.path.join(parent,filename), 'r')
            doc = fr.read()
            fr.close()
            keywords = doc.split('|')
            
            if len(keywords)>maxlen:
                maxlen = len(keywords)
            
            # wordvec = []
            # for word in keywords:
            #     if word in model.vocab:    
            #         wordvec.append( model[word].tolist() )

            # l = len(wordvec)
            # if l == 0:
            #     print 'No Words!!!___' + filename
            # else:
            #     if max_len!=None:
            #         for i in range(l, MAX_LEN):
            #             wordvec.append( [0]*VEC_DIM )

            # vec_set.append( wordvec )

    print maxlen

    return vec_set

def getLabel(dirr="classifier.txt"):
    label_set = []
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

        label_set.append( val )
        # val_dict[ val ] = val
    # print len(sorted(val_dict))
    rf.close()
    return label_set

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
    
    data = {'doc': transferUsingWord2Vec(), 'label': getLabel()}

    print 'saving data...'
    saveAsPickle(data)

    print 'over...'
    