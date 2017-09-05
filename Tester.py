import os.path
from pathlib import Path

                    # For existing File
seq=os.listdir("/Users/test/Desktop/Google/Q1")
#print (seq)
counter = 0
#
# for fileName in seq:
#     if fileName.endswith(".doc"):
#         counter += 1;
#         print("Wanted file " + str(counter) );
#
#     else:
#         print("Not wanted file");


for aFile in seq:
    if aFile.endswith(".txt"):
        print(aFile)




                    # For non existing file

# seq2 = os.listdir("/Users/test/Desktop/Google/Q2")
# print (seq2)
#
# if not os.path.exists("file2.txt"):
#     open("file2.txt", "w").close()




#Check if file exists and create if non


#fileName = Path("/Users/test/Desktop/Google/Q1/")
# if fileName.is_dir():
#     print ("Dir exist")
# else:
#     print("Dir not exist")

