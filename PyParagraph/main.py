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
    print(f'Average Letter Count: {round(letter/len(words),2)}')
    print(f'Average Sentence Lenth: {round(len(words)/len(sentences),2)}')
    print(" ")


output_file = open("Paragraph_Analysis.txt", "w")

    # write financial analysis output
output_file.write( f"""
Paragraph Analysis
-------------------------------------
Approximate Word Count: {len(words)}
Approximate Sentence Count: {len(sentences)}
Average Letter Count: {round(letter/len(words),2)}
Average Sentence Lenth: {round(len(words)/len(sentences),2)}
"""
)
