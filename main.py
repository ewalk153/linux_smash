import sys, random
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import Qt

class SmashApp(QMainWindow):
    MAX_LETTERS = 5
    labels = []

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Return:
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
        
        if len(self.labels) > self.MAX_LETTERS:
            l = self.labels.pop(0)
            l.deleteLater()

    def __init__(self, soundbank):
        super().__init__()
        self.title = 'PyQt absolute positioning - pythonspot.com'
        self.left = 10
        self.top = 10
        screen = QDesktopWidget().screenGeometry()
        
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
    LETTERS = ['A', 'H']
    NOTES = {}

    # defer setup until in a QEventLoop 
    def setup(self):
        for letter in self.LETTERS:
            self.NOTES[letter] = QSound("sounds/" + letter + ".wav")

    def play(self, letter):
        if letter in self.NOTES:
            self.NOTES[letter].play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sounds = SoundBank()
    ex = SmashApp(sounds)
    sys.exit(app.exec_())