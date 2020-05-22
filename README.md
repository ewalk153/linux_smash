## Linux Smash

A simple app to play sounds and show letters when the keyboard is used.

![screenshot](https://raw.githubusercontent.com/ewalk153/linux_smash/master/screenshot.png)

mac setup:
```bash
brew install pyqt
/usr/local/opt/python@3.8/bin/python3 -m venv venv
source venv/bin/activate
pip install -Ur requirements.txt
```

later when you come back:
```bash
source venv/bin/activate
```
linux setup:
```bash
pip install -Ur requirements.txt
sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools pulseaudio
pip install PyQt-builder
```

and to run:
```bash
python3 main.py
```
