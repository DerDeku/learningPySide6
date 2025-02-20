from ..dialog import Dialog
from ...gui.screens.gameScreen import GameScreen
from ..gameData.events.event import Event, E_Event


class DialogHandler:
    def __init__(self):
        pass    
    def startDialog(self, dialog : Dialog, gameScreen : GameScreen):
        gameScreen.console.print(dialog.startLine)
        for response in dialog.dict_npc[dialog.startLine]:
            gameScreen.addDialogOption(response, dialog.dict_player)
    