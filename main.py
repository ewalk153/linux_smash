import sys, random, string
from os import listdir
from os.path import isfile, join, splitext
from collections import defaultdict

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt6.QtGui import QIcon, QGuiApplication
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QSoundEffect

def debug_trace():
  '''Set a tracepoint in the Python debugger that works with Qt'''
  from PyQt6.QtCore import pyqtRemoveInputHook
  from pdb import set_trace
  pyqtRemoveInputHook()
  set_trace()

class SmashApp(QMainWindow):
    MAX_LETTERS = 5
    labels = []

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key.Key_Return:
            print('return key pressed')
        else:
            if self.showable(key):
                char = chr(key)
                # print('key pressed: %s' % char)
                self.showChar(char)

    def showable(self, key):
        return (key >= ord('A') and key <= ord('Z')) or (key >= ord('0') and key <= ord('9'))

    def showChar(self, char):
        color = random.choice(['red', 'green', 'blue', 'magenta', 'purple', 'green'])
        label = QLabel(char, self)
        label.resize(120, 120)
        label.move(
            random.randint(0, self.width),
            random.randint(0, self.height))
        label.setStyleSheet('color: ' + color)
        label.show()

        self.labels.append(label)
        self.sounds.play(char)
        self.show()

        self.checkForExitWord()
        
        if len(self.labels) > self.MAX_LETTERS:
            l = self.labels.pop(0)
            l.deleteLater()

    def checkForExitWord(self):
        word = []
        for l in self.labels:
            word.append(l.text())

            if word[-4:] == ["Q", "U", "I", "T"]:
                sys.exit(0)

    def __init__(self, soundbank):
        super().__init__()
        self.title = 'Linux Smash'
        self.left = 10
        self.top = 10
        screen = QGuiApplication.primaryScreen().availableGeometry()
        
        self.width = screen.width()
        self.height = screen.height()
        # self.setGeometry(0, 0, screen.width(), screen.height())

        self.showFullScreen()
        self.initUI()

        self.sounds = soundbank
        self.sounds.setup()

        self.setStyleSheet("QLabel {font: 120pt Helvetica}")
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

class SoundBank():
    LETTERS = list(string.ascii_uppercase) + list(string.digits)
    NOTES = defaultdict(list)

    # defer setup until in a QEventLoop 
    def setup(self):
        path = "sounds/"
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and splitext(f)[1] == ".wav"]
        for file in onlyfiles:
            letter = file[0].upper()
            self.NOTES[letter].append(new_sound(path + file))

    def play(self, letter):
        if letter in self.NOTES:
            random.choice(self.NOTES[letter]).play()

def new_sound(local_file):
    effect = QSoundEffect()
    effect.setSource(QUrl.fromLocalFile(local_file))
    return effect

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sounds = SoundBank()
    ex = SmashApp(sounds)
    sys.exit(app.exec())
