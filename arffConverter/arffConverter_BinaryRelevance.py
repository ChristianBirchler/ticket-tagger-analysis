import numbers
import random

if __name__ == '__main__':
    ticketTaggerDataSet = open("data_set-pandas-balanced.txt", "r+", encoding="utf-8")
    ticketTaggerContent = ticketTaggerDataSet.read()
    ticketTaggerContent = ticketTaggerContent.split("__label__")

    wekaDataSet = open("arff_notProcessed/BR-MEKA_pandas_balanced.arff", "w+", encoding="utf-8")

    wekaDataSet.write("@relation 'testFile: -C 3'\r\n")
    wekaDataSet.write("@attribute issueText string\r")
    wekaDataSet.write("@attribute __bug__ {0,1}\r")
    wekaDataSet.write("@attribute __enhancement__ {0,1}\r")
    wekaDataSet.write("@attribute __question__ {0,1}\r\n")

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
        if label == "__bug__":
            wekaDataSet.write("\"" + issueText + " \"," + "1,0,0" + "\r")
        elif label == "__enhancement__":
            wekaDataSet.write("\"" + issueText + " \"," + "0,1,0" + "\r")
        if label == "__question__":
            wekaDataSet.write("\"" + issueText + " \"," + "0,0,1" + "\r")

    wekaDataSet.close()
    ticketTaggerDataSet.close()
