from PySide6.QtWidgets import QApplication, QMainWindow
from .lib.handler.gameHandler import GameHandler


def main():
    app = QApplication()
    mainWindow = QMainWindow()
    mainWindow.show()
    gameHandler = GameHandler(mainWindow)
    gameHandler.startGame()
    
    
    
    app.exec()