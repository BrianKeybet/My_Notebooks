# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 19:36:15 2022

@author: support.user2
"""
my_sentence = 'a random sentence, this is another'
print(my_sentence.upper())
print(my_sentence.count('a'))

my_words = my_sentence.split()

print(my_words)

my_2_sentences = my_sentence.split(',')

print(my_2_sentences)


# Split string into characters
word = "a random sentence"
empty_list = []
for char in word:
    empty_list.append(char)
    
print(empty_list)

#Another way to do it
def split(word):
    return [char for char in word]
     
# Remove blank spaces
my_sentence = my_sentence.replace(" ", "")

#Assign it to word and run split function
word = my_sentence
words = split(word)
