file_object = open("files/claude.txt", "w")
for number in range(5):
    square = number * number
    file_object.write(str(square) + "\n")
    #file_object.write("\n")
file_object.close()


## using with keyword to manipulate file

with open("files/test.txt", "w") as tst:
    tst.write("Hello")
