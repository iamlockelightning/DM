# -*- coding:utf-8 -*- 

# https://www.airpair.com/nlp/keyword-extraction-tutorial
import os
import rake
import operator

def extractKeyword(doc="", ret_type='list'):
    rake_object = rake.Rake("SmartStoplist.txt", 1, 1, 1)
    # text = "BLUMENTHAL--Martin. A New York business man and philanthropist, died last Saturday in Manhattan after a long illness. He was 90. Mr. Blumenthal was born in Frankfurt, Germany and immigrated to New York City in 1935. He was President of A.J. Hollander and Company, a commodities trading firm. After retirement he devoted himself to philanthropic activities. He was a trustee of the YMHA and served as chairman of Bezalel, a charitable organization that supports the arts in Israel. He was also active in Human Rights Watch. Mr. Blumenthal is survived by his wife, Sallie Blumenthal, his children Richard of Greenwich and David of Boston, six grandchildren, his brother Fred and his sister, Edith Levisohn. His first wife Jane died in 1969. Funeral will take place at Riverside Chapel at 11:30am, Tuesday January 2nd. $(6$)BLUMENTHAL--Martin. Park Avenue Synagogue mourns the passing of a devoted congregant. We extend to his wife Sally and the entire family our heartfelt sympathy. May his memory remain for a blessing. David H. Lincoln, Sr. Rabbi Amy AB Bressman, Chairman of the Board Menachem Z. Rosensaft, President".lower()
    text = doc.lower()
    keywords = rake_object.run(text)
    if ret_type=='list':
        keywords_list = []
        for item in keywords:
            keywords_list.append(item[0])
        return keywords_list
    elif ret_type=='str':
        keywords_list = ''
        for item in keywords:
            keywords_list += item[0] + ' '
        return keywords_list[0:-1]
    else:
        return None

if __name__=="__main__":
    rawdir = "C:/Users/locke/Desktop/doc"
    keyworddir = "C:/Users/locke/Desktop/key"
    for parent,dirnames,filenames in os.walk(rawdir):
        for filename in filenames:
            if os.path.splitext(filename)[1]=='.txt':
                fr = open(os.path.join(parent,filename), 'r')
                doc = fr.read()
                fr.close()
                keywords_list = extractKeyword(doc, 'str')
                fw = open(os.path.join(keyworddir, filename+'.key'), 'w')
                fw.write(keywords_list+'\n')
                fw.close()


'''
import requests
import json

def callAPI(doc):
    data = {'appkey': '258bbb3f7adf4c0e7fb74129d59865e9', 'text': doc}
    url = 'http://qingyu.thunlp.org/api/KeywordExtract'

    r = requests.post(url, data=data)
    print r
    print r.text
    # ans = json.loads(r.text)['Result']
    # print ans
    # return ans
'''
