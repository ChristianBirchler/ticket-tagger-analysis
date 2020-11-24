#!/usr/bin/python3

import sys
import requests
import re

if __name__ == '__main__':
    print('* start ' + sys.argv[0])

    # get owner and repo names from cli
    owner = sys.argv[1]
    repo = sys.argv[2]

    username = 'ChristianBirchler'
    token = # your access token

    # get the total number of pages by making a dummy call
    URL = 'https://api.github.com/repos/' + owner + '/' + repo + '/issues?state=all'
    r = requests.get(URL, auth=(username,token))
    link_header = r.headers['link']
    m = re.findall('[0-9]+', link_header)

    # number of pages to traverse
    nr_pages = int(m[-1])

    # add 'page' parameter for API call
    URL_no_page_nr = URL + '&page='

    # all jsons are concatenated in this list
    data = []

    # iterate over all available pages and store results in 'data'
    for page_nr in range(1, nr_pages+1):
        print('* get page ' + str(page_nr))
        URL_with_page_nr = URL_no_page_nr + str(page_nr)
        res = requests.get(URL_with_page_nr, auth=(username,token))
        print('* ' + str(type(res)))
        data = data + res.json()

    print('* ' + str(len(data)) + ' issues are downloaded')

    # write data to file
    filename = owner + '-' + repo + '.json'
    print('* write data to ' + filename)
    with open (filename, 'w') as f:
        f.write(str(data))

    print('* done')

