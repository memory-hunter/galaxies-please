import json
import random

from .document import Document


class DocumentHandler:
    def __init__(self, docnum):
        self.docnum = docnum
        self.data = json.loads(open("../res/data/data.json", "r").read())
        self.mistakes = 0
        self.playdocs = random.sample(self.data, self.docnum)
        for i in range(0, len(self.playdocs)):
            x = self.data.index(self.playdocs[i])
            j = list(range(0, x)) + list(range(x+1, len(self.data)))
            self.playdocs[i] = Document(
                self.playdocs[i],
                self.data[random.choice(j)]
            ).present()
    def reinit(self):
        self.mistakes = 0
        self.playdocs = random.sample(self.data, self.docnum)
        for i in range(0, len(self.playdocs)):
            x = self.data.index(self.playdocs[i])
            j = list(range(0, x)) + list(range(x+1, len(self.data)))
            self.playdocs[i] = Document(
                self.playdocs[i],
                self.data[random.choice(j)]
            ).present()
