import pomodorro
import sys
import time

while True:
  pomodorro.tick(pomodorro.dataStruct)
  # pomodorro.onSwitch(pomodorro.dataStruct)
  sys.stdout.write(pomodorro.UI(pomodorro.dataStruct))
  sys.stdout.write("\033[K")
  sys.stdout.write("\033[F")
  sys.stdout.write("\033[K")
  sys.stdout.write("\033[F")

  
  # sys.stdout.flush()
  time.sleep(0.01)
  
