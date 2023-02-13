import json
import os
import random

import pandas as pd


class Profanity():
    def __init__(self):
        try:
            with open(os.path.join('config', 'config.json')) as config_file:
                self.profane_words = json.load(config_file)
        except:
            print("Error loading the json file of profane words")

        self.censored_text = []
        self.degree_of_profanity = []
    
    def calculate_degree_of_profanity(self, scentence):
        '''
        Takes in a scentences and gives its degree of profanity 
        and censored text
        '''
        scentence = scentence.split(" ")
        censored_scentence = []
        count_profane_words = 0
        for idx, word in enumerate(scentence):
            if word.lower() in self.profane_words[word[0].lower()]:
                count_profane_words += 1
                censored_scentence.append('*'*len(word))
            
            else:
                censored_scentence.append(word)

        self.censored_text.append(" ".join(censored_scentence))
        self.degree_of_profanity.append(count_profane_words/len(scentence))

    def print_output(self, print_flag=False):
        '''
        Print the results generated for the scentences
        '''
        
        for i in range(len(self.censored_text)):
            if print_flag:
                print("Censored Text: ", self.censored_text[i])
            print("Degree of Profanity: ", self.degree_of_profanity[i], end='\n\n')

    def save_output_csv(self, input_path, save_path):
        '''
        Takes input the save path.
        It will save the outputs in a csv file at save path
        '''

        try:
            data = pd.DataFrame({'Censored Text': self.censored_text, 'Degree of Profanity': self.degree_of_profanity})
            
            if not save_path.endswith('.csv'):
                save_path = os.path.join(save_path, os.path.basename(input_path))
            
            data.to_csv(save_path, index=False)
            print("Output csv file saved at",save_path)

        except:
            print("Error in saving csv file, Please provide correct path")
