from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel, QMainWindow, QStackedLayout, QLineEdit, QFormLayout
from PySide6.QtCore import Qt

from ...gui.screens.gameScreen import GameScreen
from ...gui.screens.characterCreationScreen import CharacterCreationScreen
from ...gui.screens.startScreen import StartScreen

class Scene:
    StartScreen = 0
    CharacterCreation = 1
    gameScreen = 2

class SceneHandler():
    def __init__(self, mainWindow : QMainWindow):
        self.mainWindow = mainWindow
        self.widget = QWidget()
        self.sceneManager = QStackedLayout()
        self.widget.setLayout(self.sceneManager)
        self.mainWindow.setCentralWidget(self.widget)
        self.gameScreen = None
        self._initStartScreen()
        self._initCharacterCreation()
        self._initGameScreen()
    
    def setSceneTo(self, scene : Scene) -> None:
        """Sets the SceneHandler.sceneManager : QStackedLayout Index to 'scene'"""
        self.sceneManager.setCurrentIndex(scene)
        
    def _initStartScreen(self) -> None:
        self.startScreen = StartScreen()        
        self.sceneManager.addWidget(self.startScreen)
    
    def _initCharacterCreation(self) -> None:
        self.characterCreationScreen = CharacterCreationScreen()
        self.sceneManager.addWidget(self.characterCreationScreen)

    def _initGameScreen(self) -> None:
        if self.gameScreen:
            self.sceneManager.removeWidget(self.gameScreen)
        self.gameScreen = GameScreen()
        self.sceneManager.addWidget(self.gameScreen)