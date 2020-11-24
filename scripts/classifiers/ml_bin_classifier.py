import json

import fasttext
import os.path
import numpy as np
from numpy import array
from sklearn.model_selection import KFold


def get_guess(res):
    labels = res[0]
    i = 0
    if labels[0] == '__label__other':
        i = 1
    return res[0][i], res[1][i]


data_set = os.path.dirname(__file__) + '/../data_set-pandas-balanced.txt'

print("Converting dataset to array")
f = open(data_set, 'r+', encoding="UTF-8")
data = array(f.readlines())
f.close()

# smaller data set
kfold = KFold(10, shuffle=True, random_state=1)
b_path_train = os.path.dirname(__file__) + '/b_tmp_train.txt'
e_path_train = os.path.dirname(__file__) + '/e_tmp_train.txt'
q_path_train = os.path.dirname(__file__) + '/q_tmp_train.txt'
path_test = os.path.dirname(__file__) + '/tmp_test.txt'

b_path = os.path.dirname(__file__) + '/../preprocessing/BUG-data_set-pandas-balanded.txt'
e_path = os.path.dirname(__file__) + '/../preprocessing/ENHANCEMENT-data_set-pandas-balanded.txt'
q_path = os.path.dirname(__file__) + '/../preprocessing/QUESTION-data_set-pandas-balanded.txt'

print("Converting bug dataset to array")
f = open(b_path, 'r+', encoding="UTF-8")
b_data = array(f.readlines())
f.close()

print("Converting enhancement dataset to array")
f = open(e_path, 'r+', encoding="UTF-8")
e_data = array(f.readlines())
f.close()

print("Converting question dataset to array")
f = open(q_path, 'r+', encoding="UTF-8")
q_data = array(f.readlines())
f.close()

fold_outputs = []

fold = 1

for train, test in kfold.split(data):

    TP_b = 0
    TP_FN_b = 0
    TP_FP_b = 0

    TP_e = 0
    TP_FN_e = 0
    TP_FP_e = 0

    TP_q = 0
    TP_FN_q = 0
    TP_FP_q = 0

    print("New tenfold iteration: ", str(fold))

    print("Creating bug train file")
    b_tmp_train = open(b_path_train, "w", encoding="UTF-8")
    for line in b_data[train]:
        b_tmp_train.write("".join(line))
    b_tmp_train.close()

    print("Creating enhancement train file")
    e_tmp_train = open(e_path_train, "w", encoding="UTF-8")
    for line in e_data[train]:
        e_tmp_train.write("".join(line))
    e_tmp_train.close()

    print("Creating question train file")
    q_tmp_train = open(q_path_train, "w", encoding="UTF-8")
    for line in q_data[train]:
        q_tmp_train.write("".join(line))
    q_tmp_train.close()

    test_data = data[test]

    print("start training...")
    # gets stuck
    b_model = fasttext.train_supervised(input=b_path_train)
    e_model = fasttext.train_supervised(input=e_path_train)
    q_model = fasttext.train_supervised(input=q_path_train)

    print("start testing for tenfold iteration...")
    for i, line in enumerate(test_data):
        t = line.partition(' ')
        issue_text = t[2].replace('\n', '').replace('\r', '')

        correct_answer = t[0]
        b_res = b_model.predict(issue_text, k=-1)
        e_res = e_model.predict(issue_text, k=-1)
        q_res = q_model.predict(issue_text, k=-1)

        b_guess = get_guess(b_res)
        e_guess = get_guess(e_res)
        q_guess = get_guess(q_res)

        res = {
            b_guess[0]: b_guess[1],
            e_guess[0]: e_guess[1],
            q_guess[0]: q_guess[1]
        }

        guess = max(res, key=res.get)

        if guess == '__label__bug':
            TP_FP_b += 1
            if guess == correct_answer:
                TP_b += 1

        if guess == '__label__enhancement':
            TP_FP_e += 1
            if guess == correct_answer:
                TP_e += 1

        if guess == '__label__question':
            TP_FP_q += 1
            if guess == correct_answer:
                TP_q += 1

        if correct_answer == '__label__bug':
            TP_FN_b += 1

        if correct_answer == '__label__enhancement':
            TP_FN_e += 1

        if correct_answer == '__label__question':
            TP_FN_q += 1

        print("Issue nr." + str(i) + " has predicted: ")
        print("Bug res: ", str(b_guess))
        print("Enhancement res: ", str(e_guess))
        print("Question res: ", str(q_guess))
        print("Final guess: ", str(guess))
        print("Correct answer: ", correct_answer)
        print("-------------------------------------------------")

    b_recall = TP_b / TP_FN_b
    b_precision = TP_b / TP_FP_b
    b_f1 = 2 * ((b_precision * b_recall) / (b_precision + b_recall))

    e_recall = TP_e / TP_FN_e
    e_precision = TP_e / TP_FP_e
    e_f1 = 2 * ((e_precision * e_recall) / (e_precision + e_recall))

    q_recall = TP_q / TP_FN_q
    q_precision = TP_q / TP_FP_q
    q_f1 = 2 * ((q_precision * q_recall) / (q_precision + q_recall))

    ges_recall = (b_recall + e_recall + q_recall) / 3
    ges_precision = (b_precision + e_precision + q_precision) / 3
    ges_f1 = (b_f1 + e_f1 + q_f1) / 3

    result = {
        '10-Fold iteration:': fold,
        'Mean f1': ges_f1,
        'Mean recall': ges_recall,
        'Mean precision': ges_precision,
        'Bug recall': b_recall,
        'Bug precision': b_precision,
        'Bug f1': b_f1,
        'Enhancement recall': e_recall,
        'Enhancement precision': e_precision,
        'Enhancement f1': e_f1,
        'Question recall': q_recall,
        'Question precision': q_precision,
        'Question f1': q_f1
    }
    print("Fold over, here are results: ")
    print(json.dumps(result, indent=4))
    fold_outputs.append(result)

    fold += 1

print("Done with 10 fold validation")

mean_recall = 0
mean_precision = 0
mean_f1 = 0
for f in fold_outputs:
    mean_f1 += (f['Mean f1'] / 10)
    mean_recall += (f['Mean recall'] / 10)
    mean_precision += (f['Mean precision'] / 10)

output = {
    'Results': {
        'F1': mean_f1,
        'Recall': mean_recall,
        'Precision': mean_precision
    },
    'Details': fold_outputs
}
print(json.dumps(output, indent=4))

# recall = TP/(TP+FN)
# recall_bug = #final guess = bug && correct answer = bug / #correct answers = bug

# precision = TP / (TP+FP)
# precision_bug = #final guess = bug && correct answer = bug / #final guess = bug

# f1 = 2*((precision*recall)/(precision+recall))
