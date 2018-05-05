import os
import string
import re
# import re
# from collections import Counter
filename = input("Please type the file name you would like to analyze, include .txt ")
paragraph_path = os.path.join('.',filename)

with open(paragraph_path, 'r') as paragraph:

    paragraph_contents = paragraph.read()


    # print(paragraph_contents)
    print(" ")
    print(f'Paragraph Analysis')
    print(f'-----------------------------')
    words = paragraph_contents.split()
    print(f'Approximate Word Count: {len(words)}')
    paragraph_contents = paragraph_contents.replace("\n", " ") + " "
    sentences  = re.split("[.!?\n] +", paragraph_contents)
    print(f'Approximate Sentence Count: {len(sentences)}')
    letter = 0
    for letters in words:
       letter += len(letters)
    print(f'Average Letter Count: {letter/len(words)}')
    print(f'Average Sentence Lenth: {len(words)/len(sentences)}')
    print(" ")