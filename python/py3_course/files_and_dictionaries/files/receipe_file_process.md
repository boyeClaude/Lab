### Recipe for Reading and Processing a File

Here’s a foolproof recipe for processing the contents of a text file. If you’ve fully digested the previous sections, you’ll understand that there are other options as well. Some of those options are preferable for some situations, and some are preferred by python programmers for efficiency reasons. In this course, though, you can always succeed by following this recipe.

#1. Open the file using with and open.

#2. Use .readlines() to get a list of the lines of text in the file.

#3. Use a for loop to iterate through the strings in the list, each being one line from the file. On each iteration, process that line of text

#4. When you are done extracting data from the file, continue writing your code outside of the indentation. Using with will automatically close the file once the program exits the with block.
