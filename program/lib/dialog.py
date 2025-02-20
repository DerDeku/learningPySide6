class Dialog:
    def __init__(self, startLine : str):
        self.startLine      = startLine
        self.dict_player    = dict()
        self.dict_npc       = dict()    
        
if __name__ == "__main__":
    dialog = Dialog()
    dialog.dict_player  = {"How are you?" : "Well good, thanks for asking friend",
                           "Fight me basterd!" : "wha.. what?$combat",
                           "Do you know what happend to Ascalon?" : "No, I stay as far away as possible from that wicked place\nBut ask Fredrick about Ascalon$newQuest<Find Fredrick>"}
    dialog.dict_npc     = {"Hi there" : ["How are you?", "Fight me bastard!"],
                           "Well good, thanks for asking friend, what are you doing here?" : ["None of your business!$combat", "I am here to trade$trade", "Do you know what happened to Ascalon?"]}

        
    
    