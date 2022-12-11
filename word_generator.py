from random import choice


class WordGenerator:
    def __init__(self):
        self.words = {}
        try:
            with open("countries_and_capitals.txt", encoding = "utf-8") as f:
                for line in f:
                    (country, capital) = line.split("/")
                    words[country.strip()] = capital.strip()
        except OSError:
            print("Oops! Could not open/read file containing countries and capitals.")
            print("Please make sure you have countries_and_capitals.txt in your folder.")
        self.hidden_word = choice(list(self.words.keys()))
