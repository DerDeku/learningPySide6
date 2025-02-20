from PySide6.QtWidgets import QVBoxLayout, QPushButton, QWidget
from PySide6.QtCore import Qt
from ...lib.handler.saveFileHandler import SaveFileHandler

class StartScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buttonStartNewGame = QPushButton("Start New Game")
        self.buttonContinueGame = QPushButton("Continue")
        self.buttonLoadGame     = QPushButton("Load Game")
        if not SaveFileHandler.hasSaves():
            self.buttonContinueGame.setEnabled(False)
        layout.addWidget(self.buttonContinueGame)
        layout.addWidget(self.buttonStartNewGame)
        layout.addWidget(self.buttonLoadGame)