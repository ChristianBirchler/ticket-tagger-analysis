#!/usr/bin/python3

import sys
import re
from nltk.corpus import stopwords

def remove_stopwords(issue):
    """
    return: a stopword removal version of the issue by
    keeping the label prefix unchanged.
    """

    # set up regex to split label (prefix) from issue (postfix)
    prefix_pattern = re.compile(r'__label__\w+')
    match = prefix_pattern.match(issue)
    prefix_ind = match.span()
    prefix = issue[prefix_ind[0]:prefix_ind[1]]
    postfix = issue[prefix_ind[1]:]

    # treat only postfix
    stopword_removed_postfix = ''
    postfix_words = re.findall(r'\w+', postfix)
    for word in postfix_words:
        if word not in stopwords.words('english'):
            stopword_removed_postfix += ' ' + word

    # return concatenation of prefix and the stemmed postfix
    return prefix + stopword_removed_postfix


if __name__ == '__main__':
    print('* start ' + sys.argv[0])
    fn_in = sys.argv[1]
    fn_out = sys.argv[2]

    # create and open output file
    f_out = open(fn_out, mode='w')

    # open data file and stem words
    with open(fn_in, mode='r') as f:
        cnt = 0
        for issue in f:
            print('* stopword removal from issue ' + str(cnt))
            f_out.write(remove_stopwords(issue) + '\n')
            cnt += 1

    # close new output file
    f_out.close()


