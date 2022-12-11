from pathlib import Path
from random import choice


filepath = Path(__file__).parent / "countries_and_capitals.txt"

class WordGenerator:
    def __init__(self):
        self.words = {}
        try:
            with open(filepath, encoding = "utf-8") as f:
                for line in f:
                    (country, capital) = line.split("/")
                    self.words[country.strip()] = capital.strip()
        except OSError:
            print("Oops! Could not open/read file containing countries and capitals.")
            print("Please make sure you have countries_and_capitals.txt in your folder.")
        self.hidden_word = choice(list(self.words.keys()))
