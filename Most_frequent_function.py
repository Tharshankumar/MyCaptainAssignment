"""
Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

Your Input and output should look something like this

Input : Please enter a string Mississippi

Output : i = 04 s = 04 p =02 m =01
"""


abc= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] -= 1
    return d

print (most_frequent(abc))
