# pomodorro-cli
This is a python pomodorro command line app.

![Here it is](/public/out.gif)

Feautures:
 - keeps track of your sessions, so you can kill it. When you start it will continue working from the same time.
 - has a beautiful timer
 - no dependencies

Install it like this:
```
git clone https://github.com/VbifRkbvjd/pomodorro-cli
```
Usage is like this
```bash
python ./main.py
```
Configuration is in **config.py**
```python
SAVE_FILE = "pomodorro.db"
WORK = 25
REST = 5
BIGREST = 25
ONE_SECOND = 1
```
If you want to make a pause. Close app by **Ctrl+c**. It will remember it last position when you start it again.



