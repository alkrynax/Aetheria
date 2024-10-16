"""
An app to manage your characters for your Aetheria's campains
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class AetheriaCompanionApp(toga.App):
    def startup(self):
        # Building the main display box
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        
        self.char_button = toga.Button('Fiches Persos')

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()


def main():
    return AetheriaCompanionApp()

def showChars(self) : 
    self.content_box.children.clear()
    self.content_box.add(toga.Label("Gestion des fiches de personnages"))
    
def showDice(self):
    self.content_box.children.clear()
    self.content_box.add(toga.Label("Lancer un dé selon le besoin"))
    
def showLore(self): 
    self.content_box.children.clear()
    self.content_box.add(toga.Label("Accéder à l'histoire et au scénario"))

def showStats(self):
    self.content_box.children.clear()
    self.content_box.add(toga.Label("Accéder aux stats du joueur"))

# Lancé de dé en prenant en compte deux params : le dé  (d6/d10/d20) etc et modifier (Bonus/Malus) 
def DiceRoll(dice,modifier) : 
    import random
    result = random.randint(1,dice)
    if (modifier >=0) :
        result+=modifier
    else: 
        result-=modifier
    return result
