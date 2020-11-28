import numbers
import random
import sys

if __name__ == '__main__':
    print('* execute ' + sys.argv[0])
    # catch missing arguments
    try:
        a1 = sys.argv[1]
        a2 = sys.argv[2]
    except IndexError as error:
        print('\033[91m' + "Could not read arguments. Please use the correct command format. Example command:")
        print("python arffConverter_Multitarget.py ./Input_Multitarget.txt ./Output_Multitarget.arff ")
        exit()
    # define paths
    f_in = sys.argv[1]
    f_out = sys.argv[2]

    ticketTaggerDataSet = open(f_in, "r+", encoding="utf-8")
    ticketTaggerContent = ticketTaggerDataSet.read()
    ticketTaggerContent = ticketTaggerContent.split("__label__")

    Multitarget_ARFF_Dataset = open(f_out, "w+", encoding="utf-8")

    Multitarget_ARFF_Dataset.write("@relation 'testFile: -C 1'\r\n")
    Multitarget_ARFF_Dataset.write("@attribute issueText string\r")
    Multitarget_ARFF_Dataset.write("@attribute tickerTaggerLabel {__bug__,__enhancement__,__question__}\r\n")

    Multitarget_ARFF_Dataset.write("@data\r\n")

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
        Multitarget_ARFF_Dataset.write("\"" + issueText + " \"," + label + "\r")

    Multitarget_ARFF_Dataset.close()
    ticketTaggerDataSet.close()
