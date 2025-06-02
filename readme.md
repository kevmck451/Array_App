# Microphone Array Application

![App Home](docs/app_display.jpeg)

---

## 1. Installation

### Mac

```zsh
git clone https://github.com/kevmck451/Array_App
```

```zsh
cd Array_App
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_mac.txt
```


### Raspberry Pi

- app would need to be broken up to split processing. a single rasp pi cannot run the app in realtime

```bash
git clone https://github.com/kevmck451/Array_App
```

```bash
cd Array_App
python3 -m venv venv
source venv/bin/activate
```
- installing on pi requires some manual installation process in order to get librosa working

```bash
pip install -r requirements_pi.txt
```

## 2. Run

```zsh
python3 main.py
```



