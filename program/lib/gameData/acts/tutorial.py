from ....gui.screens.gameScreen import GameScreen
from ...dialog import Dialog
from ...handler.dialogHandler import DialogHandler
from ..player import Player

class Tutorial:
    def __init__(self, dialogHandler : DialogHandler, gameScreen : GameScreen, player : Player):
        self.gameScreen     = gameScreen
        self.player         = player
        self.dialogHandler  = dialogHandler 
        
    def start(self):
        dialog = Dialog("Hi there")
        dialog.dict_player  = {"How are you?" : "Well good, thanks for asking friend",
                               "Fight me basterd!" : "wha.. what?$combat",
                               "Do you know what happend to Ascalon?" : "No, I stay as far away as possible from that wicked place\nBut ask Fredrick about Ascalon$newQuest<Find Fredrick>"}
        dialog.dict_npc     = {"Hi there" : ["How are you?", "Fight me bastard!"],
                               "Well good, thanks for asking friend, what are you doing here?" : ["None of your business!$combat", "I am here to trade$trade", "Do you know what happened to Ascalon?"]}
        self.dialogHandler.startDialog(dialog, self.gameScreen)
        # self.gameScreen.console.print()
        # self.gameScreen.buttonContinue
    
    
        
    