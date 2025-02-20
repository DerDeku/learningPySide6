class E_Event:
    Combat      = "Combat"
    Dialog      = "Dialog"
    Nothing     = "Nothing"
    
class Event:
    def __init__(self, eventType : E_Event):
        self.type = eventType