import ast


def format_issue(label_name, title, body):
    return labels_dict[label_name] + " " + title.replace("\n", " ").replace("\r", " ") + (
        " " + body.replace("\n", " ").replace("\r", " ") if body else "")


labels_dict = {
    "00 - Bug": "__label__bug",
    "06 - Regression": "__label__bug",
    "01 - Enhancement": "__label__enhancement",
    "01 - Wish List": "__label__enhancement",
    "33 - Question": "__label__question"
}

str = open('numpy-numpy.json', 'r', encoding='utf8').read()
data_set = open('data_set.txt', 'w', encoding='utf8')

json_file = ast.literal_eval(str)
for issue in json_file:
    if 'labels' not in issue:
        continue
    for label in issue['labels']:
        if 'name' in label:
            if label['name'] in labels_dict:
                print(format_issue(label['name'], issue['title'], issue['body']), file=data_set)
