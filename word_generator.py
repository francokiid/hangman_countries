from random import choice


class WordGenerator:
    words = {}
    with open("countries_and_capitals.txt", encoding = "utf-8") as f:
        for line in f:
            (country, capital) = line.split("/")
            words[country.strip()] = capital.strip()
    
    def get_country(self):
        return choice(list(self.words.keys()))
