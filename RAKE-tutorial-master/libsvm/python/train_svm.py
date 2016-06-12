# -*- coding:utf-8 -*- 

from svmutil import *

TRAIN_SIZE = 3000
TEST_SIZE = 1000

# Read data in LIBSVM format
y, x = svm_read_problem('dataSVM.txt')
m = svm_train(y[:TRAIN_SIZE], x[:TRAIN_SIZE], '-t 0 -c 1 -b 1')
p_label, p_acc, p_val = svm_predict(y[TRAIN_SIZE:TRAIN_SIZE+TEST_SIZE], x[TRAIN_SIZE:TRAIN_SIZE+TEST_SIZE], m, '-b 1')

print p_acc


# Options：可用的选项即表示的涵义如下
# -s svm类型：SVM设置类型(默认0)
# 0 -- C-SVC
# 1 --v-SVC
# 2 – 一类SVM
# 3 -- e -SVR
# 4 -- v-SVR

# -t 核函数类型：核函数设置类型(默认2)
# 0 – 线性：u'v
# 1 – 多项式：(r*u'v + coef0)^degree
# 2 – RBF函数：exp(-gamma|u-v|^2)
# 3 –sigmoid：tanh(r*u'v + coef0)

# -d degree：核函数中的degree设置(针对多项式核函数)(默认3)
# -g r(gama)：核函数中的gamma函数设置(针对多项式/rbf/sigmoid核函数)(默认1/ k)
# -r coef0：核函数中的coef0设置(针对多项式/sigmoid核函数)((默认0)
# -c cost：设置C-SVC，e -SVR和v-SVR的参数(损失函数)(默认1)
# -n nu：设置v-SVC，一类SVM和v- SVR的参数(默认0.5)
# -p p：设置e -SVR 中损失函数p的值(默认0.1)
# -m cachesize：设置cache内存大小，以MB为单位(默认40)
# -e eps：设置允许的终止判据(默认0.001)
# -h shrinking：是否使用启发式，0或1(默认1)
# -wi weight：设置第几类的参数C为weight*C(C-SVC中的C)(默认1)
# -v n: n-fold交互检验模式，n为fold的个数，必须大于等于2
# 其中-g选项中的k是指输入数据中的属性数。option -v 随机地将数据剖分为n部
# -b probability_estimates: whether to traina SVC or SVR model for probability estimates, 0 or 1 (default 0)（如果需要估计分到每个类的概率，则需要设置这个）


# Construct problem in python format
# Dense data
# y, x = [1,-1], [[1,0,1], [-1,0,-1]]
# Sparse data
# >>> y, x = [1,-1], [{1:1, 3:1}, {1:-1,3:-1}]
# >>> prob  = svm_problem(y, x)
# >>> param = svm_parameter('-t 0 -c 4 -b 1')
# >>> m = svm_train(prob, param)

# Precomputed kernel data (-t 4)
# Dense data
# >>> y, x = [1,-1], [[1, 2, -2], [2, -2, 2]]
# Sparse data
# >>> y, x = [1,-1], [{0:1, 1:2, 2:-2}, {0:2, 1:-2, 2:2}]
# isKernel=True must be set for precomputer kernel
# >>> prob  = svm_problem(y, x, isKernel=True)
# >>> param = svm_parameter('-t 4 -c 4 -b 1')
# >>> m = svm_train(prob, param)
# For the format of precomputed kernel, please read LIBSVM README.


# Other utility functions
# svm_save_model('heart_scale.model', m)
# m = svm_load_model('heart_scale.model')
# p_label, p_acc, p_val = svm_predict(y, x, m, '-b 1')
# ACC, MSE, SCC = evaluations(y, p_label)

# The low-level use directly calls C interfaces imported by svm.py. Note that
# all arguments and return values are in ctypes format. You need to handle them
# carefully.
# >>> from svm import *
# >>> prob = svm_problem([1,-1], [{1:1, 3:1}, {1:-1,3:-1}])
# >>> param = svm_parameter('-c 4')
# >>> m = libsvm.svm_train(prob, param) # m is a ctype pointer to an svm_model
# Convert a Python-format instance to svm_nodearray, a ctypes structure
# >>> x0, max_idx = gen_svm_nodearray({1:1, 3:1})
# >>> label = libsvm.svm_predict(m, x0)
