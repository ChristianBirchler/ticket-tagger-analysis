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

guesses = []
for train, test in kfold.split(data):
    print("New tenfold iteration +++++++++++++++++++++++++++++++++++++++++++")
    guess_iter = np.empty(len(data[test]))

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
        # print(issue_text)
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

        if guess == correct_answer:
            guess_iter[i] = 1
        else:
            guess_iter[i] = 0

        print("Issue nr." + str(i) + " has predicted: ")
        print("Bug res: ", str(b_guess))
        print("Enhancement res: ", str(e_guess))
        print("Question res: ", str(q_guess))
        print("Final guess: ", str(guess))
        print("Correct answer: ", correct_answer)
        print("-------------------------------------------------")
    guesses.append(guess_iter)

print("Done with 10 fold validation")
print("Final guess matrix:")
print(guesses)

# recall = TP/(TP+FN)
# recall_bug = #final guess = bug && correct answer = bug / #correct answers = bug

# precision = TP / (TP+FP)
# precision_bug = #final guess = bug && correct answer = bug / #final guess = bug

# f1 = 2*((precision*recall)/(precision+recall))


# store in array and display average

