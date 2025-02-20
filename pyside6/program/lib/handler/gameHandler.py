from ...gui.screens.gameScreen import GameScreen
from ..gameData.player import Player
from .sceneHandler import SceneHandler, Scene
from .saveFileHandler import SaveFileHandler

class GameHandler:
    def __init__(self, mainWindow):
        SaveFileHandler.addGameHandler(self)
        self.sceneHandler   : SceneHandler          = SceneHandler(mainWindow)
        self.player         : None | Player         = None

    def startGame(self):
        self.showStartMenu()

    def showStartMenu(self):
        self.sceneHandler.setSceneTo(Scene.StartScreen)
        self.sceneHandler.startScreen.buttonStartNewGame.clicked.connect(self.startCharacterCreation)
        self.sceneHandler.startScreen.buttonContinueGame.clicked.connect(self.continueGame)
    
    def startCharacterCreation(self):
        self.sceneHandler.setSceneTo(Scene.CharacterCreation)
        self.sceneHandler.characterCreationScreen.buttonContinueCharacterCreation.clicked.connect(self.finishCharacterCreation)
    
    def finishCharacterCreation(self):
        self.player = self.sceneHandler.characterCreationScreen.getPlayer()
        self.sceneHandler._initGameScreen()
        self.showGameScreen()
    
    def continueGame(self):
        SaveFileHandler.load()
        self.showGameScreen()
    
    def showGameScreen(self):
        self.sceneHandler.setSceneTo(Scene.gameScreen)
        self.sceneHandler.gameScreen.buttonSave.clicked.connect(SaveFileHandler.save)
        self.sceneHandler.gameScreen.buttonMainMenu.clicked.connect(self.showStartMenu)
        self.sceneHandler.gameScreen.console.print(f"Hi there {self.player.name}")
        
