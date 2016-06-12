# DM
dm

####文件说明
数据集
doc/: 经任淼淼淼淼处理过的原文本数据，需自己下载
DM\RAKE-tutorial-master\classifier.txt: 原文本数据的标签
vectors_100.bin: word2vec模型

预处理
DM\RAKE-tutorial-master\make_SVM_data.py: 产生适用于libSVM的数据预处理脚本，输出为dataSVM.txt
DM\RAKE-tutorial-master\make_word2vec_data.py: 使用100维的word2vec，将提取出的关键词转换为100维的词向量，输出为pkl

分类脚本
DM\RAKE-tutorial-master\libsvm\python\train_svm.py: 给定dataSVM.txt，使用svm分类，参数可调


缺少的库都可pip安装，除了rake，这个文件夹就有rake，看起来很乱，但是，真安不上也没办法只能这样用……
