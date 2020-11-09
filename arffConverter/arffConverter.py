import numbers
import random

if __name__ == '__main__':
    ticketTaggerDataSet = open("rafaels-rebalanced-dataset-partial-english.txt", "r+", encoding="utf-8")
    ticketTaggerContent = ticketTaggerDataSet.read()
    ticketTaggerContent = ticketTaggerContent.split("__label__")

    wekaDataSet = open("meka_rafaels-rebalanced-dataset-partial-english.arff", "w+", encoding="utf-8")

    wekaDataSet.write("@relation 'testFile: -C 1'\r\n")
    wekaDataSet.write("@attribute issueText string\r")
    wekaDataSet.write("@attribute tickerTaggerLabel {__bug__,__enhancement__,__question__}\r\n")

    wekaDataSet.write("@data\r\n")

    for issue in ticketTaggerContent[1:]:
        label = "invalidLabel"
        issueText = issue
        startingCharacter = issue[:1]
        if startingCharacter == "b":
            issueText = issueText[4:]
            label = "__bug__"
        if startingCharacter == "q":
            issueText = issueText[9:]
            label = "__question__"
        if startingCharacter == "e":
            issueText = issueText[12:]
            label = "__enhancement__"

        issueText = issueText.replace("\"", "")
        issueText = issueText.replace("`", "")
        issueText = issueText.replace("'", "")
        issueText = issueText.replace("\n", "")
        issueText = issueText.replace("\r", "")
        issueText = issueText
        wekaDataSet.write("\""+issueText+" \","+label+"\r")

    wekaDataSet.close()
    ticketTaggerDataSet.close()
