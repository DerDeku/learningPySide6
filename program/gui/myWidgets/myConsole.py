from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import QTimer

class MyConsole(QTextEdit):
    print_delay = 35
    skip_words = False

    def __init__(self):
        super().__init__()
        self.letters = []

    def print(self, string : str):
        if self.skip_words:
            self.print_word_by_word(string)
        else:
            self.print_letter_by_letter(string)

    def print_letter_by_letter(self, string : str):
        self.letters = list(string)
        self.timer = QTimer()
        self.timer.timeout.connect(self.print_next_letter)
        self.timer.start(self.print_delay)

    def print_next_letter(self):
        if self.letters:
            self.insertPlainText(self.letters.pop(0))
        else:
            self.timer.stop()
        
    
    def print_word_by_word(self, string : str):
        self.letters = [x + " " for x in string.split()]
        self.timer = QTimer()
        self.timer.timeout.connect(self.print_next_letter)
        self.timer.start(self.print_delay)