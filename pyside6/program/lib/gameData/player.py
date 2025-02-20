from ...lib.enums.saveFile.e_player import E_Player

class Player:
    def __init__(self):
        self._name      : None | str        = None

        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def getDict(self) -> dict:
        dict_player = {E_Player.Name : self._name}
        return dict_player
    
    def loadFromDict(self, dict_player : dict):
        self._name = dict_player[E_Player.Name]