import ast


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

str = open('pandas-dev-pandas.json', 'r', encoding='utf8').read()
data_set = open('data_set-pandas.txt', 'w', encoding='utf8')

json_file = ast.literal_eval(str)
for issue in json_file:
    if 'labels' not in issue:
        continue
    for label in issue['labels']:
        if 'name' in label:
            if label['name'] in labels_dict:
                print(format_issue(label['name'], issue['title'], issue['body']), file=data_set)
