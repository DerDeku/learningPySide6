from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PySide6.QtCore import Qt

from ..myWidgets.myConsole import MyConsole


class GameScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QVBoxLayout(self)
        self.console = MyConsole()
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.console)
        self.buttonSave     = QPushButton("Save")
        self.buttonMainMenu = QPushButton("Main Menu")
        self.mainLayout.addWidget(self.buttonSave)
        self.mainLayout.addWidget(self.buttonMainMenu)
