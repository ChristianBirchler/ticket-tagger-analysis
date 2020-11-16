#!/usr/bin/python3

import sys
import re


def only(issue, label):
    prefix_pattern = re.compile(r'__label__\w+')
    match = prefix_pattern.match(issue)
    prefix_ind = match.span()
    prefix = issue[prefix_ind[0]:prefix_ind[1]]
    postfix = issue[prefix_ind[1]:]

    if prefix == '__label__' + label:
        new_prefix = '__label__' + label
    else:
        new_prefix = '__label__other'

    return new_prefix + postfix


if __name__ == '__main__':
    print('* execute ' + sys.argv[0])

    fn_in = sys.argv[1]

    f_out_bug = open('BUG-' + fn_in, mode='w')
    f_out_enhancement = open('ENHANCEMENT-' + fn_in, mode='w')
    f_out_question = open('QUESTION-' + fn_in, mode='w')

    with open(fn_in, mode='r') as f:
        cnt = 0
        for issue in f:
            print('* check label of issue ' + str(cnt))
            f_out_bug.write(only(issue, 'bug'))
            f_out_enhancement.write(only(issue, 'enhancement'))
            f_out_question.write(only(issue, 'question'))
            cnt += 1


    f_out_bug.close()
    f_out_enhancement.close()
    f_out_question.close()
