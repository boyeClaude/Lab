'''
    Learning goal:
    To understand the structure of file systems
    To understand opening files with different modes
    To introduce files as another kind of sequence that one can iterate over
    To introduce the read/transform/write pattern
    To introduce parallel assignment to two or three variables

    Objectives:
    Demonstrate that you can read a single value from each line in a file
    Convert the line to the appropriate value
    Read a line and convert it into multiple values using split and assignment to multiple variables
'''


fileref = open("files/info.txt", "r")
#contents = fileref.read()
#print("content of the file : ", contents[:20]) 


#read text file line by line
lines = fileref.readlines()
print(lines[:5])
print(len(lines))
# for line in lines:
#     print("line: ",line)
# fileref.close()
