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
sudo apt-get install qt6-base-dev pulseaudio
```

and to run:
```bash
python3 main.py
```

### Adding new audio files

I use the mac Memo app to record audio files, which creates a m4a file. To convert this to a wave file, use the following ffmpeg command:
```
ffmpeg -i inputFilename.m4a OutputFilename.wav
```
