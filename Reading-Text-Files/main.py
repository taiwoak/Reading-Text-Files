# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename


def read_file_content(filename):
    # [assignment] Add your code here
    filename = open("story.txt", "r")
    return filename.read()
print(read_file_content("filename"))


def count_words(text):
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    counts = dict()
    words = text.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( count_words("text"))
