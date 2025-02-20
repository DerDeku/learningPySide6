from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFormLayout
from PySide6.QtCore import Qt

from ..myWidgets.myConsole import MyConsole
from ...lib.gameData.player import Player
from ...lib.enums.constants import DEBUG

class CharacterCreationScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        formLayout = QFormLayout()
        formLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sceneLabel = QLabel("Character Creation")
        nameLabel = QLabel("Select Name")
        self.nameEdit = QLineEdit()
        if DEBUG:
            self.nameEdit.setText("Deku")
        self.buttonContinueCharacterCreation = QPushButton("next")
        layout.addWidget(self.buttonContinueCharacterCreation)
        layout.addWidget(sceneLabel)
        layout.addLayout(formLayout)
        formLayout.addRow(nameLabel, self.nameEdit)
        
    def getPlayer(self) -> Player:
        player = Player()
        player.name = self.nameEdit.text()
        return player