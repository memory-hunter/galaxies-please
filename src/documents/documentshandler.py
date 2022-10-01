import json

import pygame
import random
import document


class DocumentsHandler:
    def __init__(self, docnum):
        self.docnum = docnum
        self.data = json.loads(open("objects.json", "r").read())
        self.playing = False

    def play(self):
        self.playing = True
        mistakes = 0
        playdocs = random.sample(self.data, self.docnum)
        for i in range(0,len(playdocs)):
            x = self.data.index(playdocs[i])
            j = list(range(0,x)) + list(range(x+1,len(self.data)))
            playdocs[i] = document.Document(playdocs[i],self.data[random.choice(j)]).present()

        while self.playing:
            round = playdocs[0].arrayfy()
            print(round)
            action = input("type acc to Accept, den to Deny: \n")
            if action == "acc":
                if not round[-1]:
                    mistakes += 1
                playdocs.pop(0)

            elif action == "den":
                if round[-1]:
                    mistakes += 1
                playdocs.pop(0)

            if mistakes >= 3:
                return False
            if len(playdocs) == 0:
                print(mistakes)
                return True




do = DocumentsHandler(7)
if do.play():
    print("congrats")
else:
    print("you loose")