import os
import re
from collections import Counter


from collections import Counter
import re
files=os.listdir("/Users/test/Desktop/Google/Q1")

#Checks for frequency of each word
def getwordbins(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt

def removegarbage(str):
    # Replace one or more non-word (non-alphanumeric) chars with a space
    str = re.sub(r'\W+', ' ', str)
    str = str.lower()
    return str


#Opens file and reads content
def openfile(filename):
    fh = open(filename, "r+")
    str = fh.read()
    fh.close()
    return str

#Calls other already defined funtions. Code starts running from here calling functions above this line
def main(filename, topwords):
    txt = openfile(filename)
    txt = removegarbage(txt)
    words = txt.split(' ')
    bins = getwordbins(words)
    for key, value in bins.most_common(topwords):
        yield key, value

        #print(key, value)
        #return (key, value)




                                # RED APE MODIFICATION

#check whether file to write into exists oterhwise create one
if not os.path.exists("file5.txt"):
    with open("file5.txt", "w") as f1:
        #read from file
        for aFile in files:
            if aFile.endswith(".doc"):
                for word,freq in main(aFile, 1000):
                    f1.write('%s\t%d\n' % (word, freq))





                            #Below is sample of old Code which was repeated 20 times
# with open("/Users/test/PycharmProjects/ProfZainab-QueryDoc/Q1/Q1-Doc1.txt", "w") as f1:
#     for word,freq in main('/Users/test/PycharmProjects/ProfZainab-QueryDoc/Q1/newFile1.txt', 1000):
#         f1.write('%s\t%d\n' % (word, freq))
