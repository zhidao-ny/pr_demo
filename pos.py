# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:49:36 2019

@author: LiuEC
"""

import nltk
nltk.download()

def POS_method(token):
    def get_words(url):
        import requests
        words = requests.get(url).content.decode('latin-1')
        word_list = words.split('\n')
        index = 0
        while index < len(word_list):
            word = word_list[index]
            if ';' in word or not word:
                word_list.pop(index)
            else:
                index += 1
        return word_list
    
    #english_1000_words_url = 'https://gist.githubusercontent.com/deekayen/4148741/raw/01c6252ccc5b5fb307c1bb899c95989a8a284616/1-1000.txt'   
    english_1000_words_url = 'https://raw.githubusercontent.com/mahsu/IndexingExercise/master/5000-words.txt'
    #english_1000_words_url = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt'
    english_1000_words = get_words(english_1000_words_url)
    
    No_use_words = ['thorough','cs','fundamentals','engineers',
                    'candidate:','check-in','discover','companies',
                    'define','bs','ms',"adobe's",
                    'life','evaluate','ensure']
    
    total_filter_words = english_1000_words + No_use_words
    
    the_token = list(set(token))
    tagged = nltk.pos_tag(the_token)
    Pre_output = []
    for i in range(len(tagged)):
        if tagged[i][1] == 'NNP':
            Pre_output.append(tagged[i][0])
    SKILL_output = []
    for word in Pre_output:
        if (word.lower()) not in total_filter_words:
            SKILL_output.append(word)
    
    return SKILL_output
