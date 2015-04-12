import pickle
import sys
import os
import time
from config import *




SAVE_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), SAVE_FILE)
# deps: libnotify-bin
# UI:
# worked 5 pomodorros so far. Great job!
# ######------------------
# Rest after 19 min. 43 sec
# Rest now ?[Enter]

dataStruct = {
  "elapsed_time":[WORK,0],
  "total_time":  [WORK,0],
  "session":     1,
  "isWork":True
}

class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[32m'
    FAIL =    "\033[31m"
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# @TESTED
def countDown(minute_int,second_int):
  # return string[]|[minute_int,second_int]
  if second_int == 0 and minute_int == 0:
    return ["switch","switch"]
  if second_int == 0 and minute_int !=0:
    return [minute_int-1,59]
  if second_int != 0 and minute_int !=0:
    return [minute_int,second_int-1]
  if minute_int == 0 and second_int != 0:
    return [minute_int,second_int-1]
  
# @TESTED  
def ifLongBreak(pomodorro_int):
  # return boolean
  return (pomodorro_int % 4) == 0

def tick(data):
  # data => data
  elapsedMinute,elapsedSecond = countDown(*data["elapsed_time"])
  # print elapsedMinute,elapsedSecond
  if elapsedMinute == "switch":
    if data["isWork"] == True:
      if ifLongBreak(data["session"])==True:
        data["isWork"] = False
        data["elapsed_time"] = [BIGREST,0]
        data["total_time"]   = [BIGREST,0]
      else:
        data["isWork"] = False
        data["elapsed_time"] = [REST,0]
        data["total_time"]   = [REST,0]
    elif data['isWork'] == False:
        data["isWork"] = True
        data["elapsed_time"] = [WORK,0]
        data["total_time"]   = [WORK,0]
        data["session"]+=1
  else:
    data["elapsed_time"] = [elapsedMinute,elapsedSecond]

def onSwitch(data):
  # data => user action needed
  elapsedMinute,elapsedSecond = countDown(*data["elapsed_time"])
  if elapsedMinute == "switch":
    # sys.stdout.write("\033[F")
    # sys.stdout.write("\033[K")
    # sys.stdout.write("\033[F")
    # sys.stdout.write("\033[K")    
    # sys.stdout.write("\033[F")
    # sys.stdout.write("\033[K")        
    if data["isWork"] == True:
      raw_input("You should  rest! [Enter]")
    else:
      raw_input("Let's go back to work! [Enter]")
      
def get_data():
  try:
    return pickle.load(open(SAVE_FILE, "rb" ))
  except IOError:
    return dataStruct
  
def set_data(x):
  pickle.dump(x, open( SAVE_FILE, 'w+' ))

def UI_progressBar(minutesLast_int,minutesWorked_int,isWork_bool):#string
  progressBar =  minutesWorked_int*"#" + minutesLast_int*"-"
  if isWork_bool:
    return bcolors.FAIL + progressBar + bcolors.ENDC
  else:
    return bcolors.OKGREEN + progressBar + bcolors.ENDC
  return progressBar

def UI_heading(workedPomodorros_int):#string
  workedPomodorros_str = str(workedPomodorros_int)
  if workedPomodorros_int == 1:
    returnData =  "worked " +workedPomodorros_str+" pomodorro so far. Keep going!"
  elif workedPomodorros_int == 0:
    returnData =  "working your first pomodorro. Keep going!"
  elif workedPomodorros_int > 1000:
    returnData =  "You must be kidding.  You are the best hardworker I've ever seen. " + workedPomodorros_str + " pomodorros. Awesome! "
  elif workedPomodorros_int > 100:
    returnData = "You are the  best pomodorror. Write author at mklimoff222 at gmail.com to be posted in GreatPomodorrors list. " +\
            workedPomodorros_str + " pomodorros.  Awesome! "
  elif workedPomodorros_int > 10:
    returnData =  "Ohoho. You worked more than " + workedPomodorros_str + " pomodorros. Great job! Keep going "
  else:
    returnData = "You are on your first decade. Keep going. " + workedPomodorros_str + " pomodorros.  "
  return bcolors.HEADER + returnData + bcolors.ENDC

def UI_bottom(minute_int,second_int,isWork_bool):
  bottom = str(minute_int) + " min. And " + str(second_int) + " seconds"
  if isWork_bool:
    return bcolors.FAIL +  "Rest after: " + bottom + bcolors.FAIL
  else:
    return bcolors.OKGREEN + "Work after: " + bottom + bcolors.ENDC

def UI(x):
  # return string
  # UI:
  # worked 5 pomodorros so far. Great job!
  # ######------------------
  # Rest after 19 min. 43 sec
  # Rest now ?[Enter]
  minutesLast_int   = x["elapsed_time"][0]
  minutesWorked_int = x["total_time"][0] - minutesLast_int
  
  heading       = UI_heading(x["session"])
  progressBar   = UI_progressBar(minutesLast_int,minutesWorked_int,x["isWork"])
  bottom        = UI_bottom(x["elapsed_time"][0],x["elapsed_time"][1],x["isWork"])
  
  return "\n".join([heading,progressBar,bottom])

def clearSTDOut():
  sys.stdout.write("\033[K")
  sys.stdout.write("\033[F")
  sys.stdout.write("\033[K")
  sys.stdout.write("\033[F")


if __name__ == "__main__":
  while True:
    dataStruct = get_data()
    tick(dataStruct)
    sys.stdout.write(UI(dataStruct))
    set_data(dataStruct)
    del dataStruct
    clearSTDOut()
    time.sleep(ONE_SECOND)
