# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:04:26 2017

@author: zcao
"""

text = "This is a text testing string. In this case study, we will find and plot the distribution of word frequencies for each translation of Hamlet. Perhaps the distribution of word frequencies of Hamlet depends on the translation --- let's find out!"

def count_words(text):    
    text = text.lower()
    skips = [".",",",";",":","'",'"']
    for ch in skips:
        text = text.replace(ch,"")
    
    
    word_counts = {}
    for word in text.split(" "):
        # known word
        if word in word_counts:
            word_counts[word] +=1
        # unkonwn word
        else:
            word_counts[word] = 1
    return word_counts
        

from collections import Counter

def count_words_fast(text):
    
    text = text.lower()
    skips = [".",",",";",":","'",'"']
    for ch in skips:
        text = text.replace(ch,"")    
    word_counts = Counter(text.split(" "))
    return word_counts


def read_book(title_path):
    """Read a book and return a string"""
    with open(title_path,"r", encoding = "utf_8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text



def word_states(word_counts):
    """Return number of unique words and frequencies.
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return(num_unique,counts)



import os
import pandas as pd 
#book_dir = "./books"
book_dir = "."

stats = pd.DataFrame(columns = ("Language","author","title","length","unique"))
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" +language):
        for title in os.listdir(book_dir+ "/" + language + "/" author):
            inputfile = book_dir+ "/" + language + "/" author + "/" + title
            print(inputfile)    
            text = read_book(inputfile)
            (num_unique,counts) = word_states(count_words(text))
            stats.loc[title_num] = language,author.capitalize(),title.replace(".txt",""),sum(counts),num_unique
            title_num +=1
            
            
            

text = read_book("./Romeo and Juliet.txt")

ind = text.find("What's")
sample_text = text[ind:ind+100]

word_counts = count_words(text)
(num_unique,counts) = word_states(word_counts)

print((num_unique,sum(counts)))

###############


table = pd.DataFrame(columns = ("name","age"))

table.loc[1] = "James",22
table.loc[2] = "Jess",32



import matplotlib.pyplot as plt

#plt.figure(figsize = (3,3))









