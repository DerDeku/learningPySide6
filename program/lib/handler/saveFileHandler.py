import json, os, sys
from ..gameData.player import Player
from ..enums.saveFile.e_saveFile import E_SaveFile
from ..enums.constants import SAVE_FILE_FOLDER_PATH
SAVE_FILE_PATH = f"{SAVE_FILE_FOLDER_PATH}/save.json"
class SaveFileHandler:

    @classmethod
    def hasSaves(cls) -> bool:
        return os.path.isfile(SAVE_FILE_PATH)

    @classmethod
    def addGameHandler(cls, gameHandler):
        from .gameHandler import GameHandler
        cls.gameHandler : GameHandler
        cls.gameHandler = gameHandler
        
    @classmethod
    def save(cls):
        dict_save = dict()
        dict_save.setdefault(E_SaveFile.Player, cls.gameHandler.player.getDict())
        json_save = json.dumps(dict_save, indent=4)
        with open(SAVE_FILE_PATH, "w+") as file:
            file.write(json_save)
            
    # ======================== LOAD ========================
    @classmethod
    def load(cls):
        with open(SAVE_FILE_PATH, "r+") as file:
            json_save = file.read()
        dict_save = json.loads(json_save)
        
        cls._load_player(dict_save[E_SaveFile.Player])

    @classmethod
    def _load_player(cls, dict_player : dict) -> Player:
        cls.gameHandler.player = Player()
        cls.gameHandler.player.loadFromDict(dict_player)