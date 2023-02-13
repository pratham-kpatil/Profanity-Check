import json

class Profanity():
    def __init__(self):
        try:
            with open('config\\config.json') as config_file:
                self.profane_words = json.load(config_file)
        except:
            print("Error loading the json file of profane words")

        self.censored_text = []
        self.degree_of_profanity = []
    
    def calculate_degree_of_profanity(self, scentence):
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
        for i in range(len(self.censored_text)):
            print(str(i+1)+'.')
            if print_flag:
                print("Censored Text: ", self.censored_text[i])
            print("Degree of Profanity: ", self.degree_of_profanity[i], end='\n\n')