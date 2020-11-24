import ast
import sys
import os


def format_issue(label_name, title, body):
    return labels_dict[label_name] + " " + title.replace("\n", " ").replace("\r", " ") + (
        " " + body.replace("\n", " ").replace("\r", " ") if body else "")


labels_dict = {
    "Bug": "__label__bug",
    "Regression": "__label__bug",
    "Enhancement": "__label__enhancement",
    "Performance": "__label__enhancement",
    "Usage Question": "__label__question"
}

if __name__ == '__main__':

    print('* execute ' + sys.argv[0])
    # catch missing arguments
    try:
        a1 = sys.argv[1]
        a2 = sys.argv[2]
    except IndexError as error:
        print('\033[91m' + "Could not read arguments. Please use the correct command format. Example command:")
        print("python json2fasttext.py in.json out.txt")
        exit()

    # get args
    dump = sys.argv[1]
    fn_dump = os.path.basename(dump)
    f_out = sys.argv[2]

    # get files
    str = open(dump, 'r', encoding='utf8').read()
    data_set = open(f_out, 'w', encoding='utf8')

    # translate
    json_file = ast.literal_eval(str)
    for issue in json_file:
        if 'labels' not in issue:
            continue
        for label in issue['labels']:
            if 'name' in label:
                if label['name'] in labels_dict:
                    print(format_issue(label['name'], issue['title'], issue['body']), file=data_set)
