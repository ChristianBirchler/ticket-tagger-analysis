import fasttext
import os.path
import numpy as np
from numpy import array
from sklearn.model_selection import KFold

data_set = os.path.dirname(__file__) + '/../data_set-pandas-balanced.txt'

f = open(data_set, 'r+', encoding="UTF-8")
data = array(f.readlines())
f.close()

# smaller data set
kfold = KFold(10, shuffle=True, random_state=1)
i = 1
path_train = os.path.dirname(__file__) + '/tmp_train.txt'
path_test = os.path.dirname(__file__) + '/tmp_test.txt'
for train, test in kfold.split(data):

    model_save_path=os.path.dirname(__file__) + '/autotuned_model_'+str(i)+'.txt'

    tmp_train = open(path_train, "w", encoding="UTF-8")
    for line in data[train]:
        tmp_train.write("".join(line))
    tmp_train.close()

    tmp_test = open(path_test, "w", encoding="UTF-8")
    for line in data[test]:
        tmp_test.write("".join(line))
    tmp_test.close()

    print("start training...")
    # gets stuck
    model = fasttext.train_supervised(input=path_train, autotuneValidationFile=path_test, autotuneDuration=600)
    print("saving model...")
    model.save_model(model_save_path)
    print("start testing...")
    res = model.test(path_test)
    precision = res[1]
    recall = res[2]
    # store in array and display average
    f1 = 2*((precision*recall)/(precision+recall))
    print("10 fold iteration:", i)
    print("f1 score: ", f1)
    i += 1
