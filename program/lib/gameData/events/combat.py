from .event import Event, E_Event
from ....gui.myWidgets.myConsole import MyConsole

class Combat(Event):
    def __init__(self, enemies : list, rewards : list, console : MyConsole):
        super().__init__(E_Event.Combat)
        console.print("Combat")
        