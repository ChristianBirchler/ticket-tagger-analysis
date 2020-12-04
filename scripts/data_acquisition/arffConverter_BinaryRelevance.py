import os
import sys

if __name__ == '__main__':
    print('* execute ' + sys.argv[0])
    # catch missing arguments
    try:
        a1 = sys.argv[1]
        a2 = sys.argv[2]
    except IndexError as error:
        print('\033[91m' + "Could not read arguments. Please use the correct command format. Example command:")
        print("python arffConverter_BinaryRelevance.py ./Input_BinaryRelevance.txt ./Output_BinaryRelevance.arff ")
        exit()
    # define paths
    f_in = sys.argv[1]
    f_out = sys.argv[2]

    ticketTaggerDataSet = open(f_in, "r+", encoding="utf-8")
    ticketTaggerContent = ticketTaggerDataSet.read()
    ticketTaggerContent = ticketTaggerContent.split("__label__")

    BR_ARFF_Dataset = open(f_out, "w+", encoding="utf-8")

    BR_ARFF_Dataset.write("@relation 'testFile: -C 3'\r\n")
    BR_ARFF_Dataset.write("@attribute issueText string\r")
    BR_ARFF_Dataset.write("@attribute __bug__ {0,1}\r")
    BR_ARFF_Dataset.write("@attribute __enhancement__ {0,1}\r")
    BR_ARFF_Dataset.write("@attribute __question__ {0,1}\r\n")

    BR_ARFF_Dataset.write("@data\r\n")

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
            BR_ARFF_Dataset.write("\"" + issueText + " \"," + "1,0,0" + "\r")
        elif label == "__enhancement__":
            BR_ARFF_Dataset.write("\"" + issueText + " \"," + "0,1,0" + "\r")
        if label == "__question__":
            BR_ARFF_Dataset.write("\"" + issueText + " \"," + "0,0,1" + "\r")

    BR_ARFF_Dataset.close()
    ticketTaggerDataSet.close()
