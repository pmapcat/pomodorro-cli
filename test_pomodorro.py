
import pytest
import pomodorro
import sys
import os

def test_countDown():
  assert pomodorro.countDown(25,0)   == [24,59]
  assert pomodorro.countDown(0,0)    == ["switch","switch"]
  assert pomodorro.countDown(0,1)    == [0,0]
  assert pomodorro.countDown(23,34)  == [23,33]
  assert pomodorro.countDown(2,0)    == [1,59]
  assert pomodorro.countDown(0,34)   == [0,33]

def test_ifLongBreak():
  assert pomodorro.ifLongBreak(1) == False
  assert pomodorro.ifLongBreak(2) == False
  assert pomodorro.ifLongBreak(3) == False
  assert pomodorro.ifLongBreak(4) == True
  assert pomodorro.ifLongBreak(5) == False
  assert pomodorro.ifLongBreak(6) == False
  assert pomodorro.ifLongBreak(7) == False
  assert pomodorro.ifLongBreak(8) == True
  assert pomodorro.ifLongBreak(9) == False
  assert pomodorro.ifLongBreak(10) == False
  assert pomodorro.ifLongBreak(11) == False
  assert pomodorro.ifLongBreak(12) == True
def test_dataLoadFlush():
  try:
    os.remove(pomodorro.SAVE_FILE)
  except:
    pass
  assert pomodorro.get_data() == pomodorro.dataStruct
  pomodorro.dataStruct["beshko"] = True
  pomodorro.set_data(pomodorro.dataStruct)
  pomodorro.dataStruct["beshko"] = False
  assert pomodorro.get_data()['beshko'] == True
  try:
    os.remove(pomodorro.SAVE_FILE)
  except:
    pass
  

  
  
  
  

# def test_UI():
#   for i in range(1,100000):
#     pomodorro.tick(pomodorro.dataStruct)
#     sys.stdout.write("\r" + pomodorro.UI(pomodorro.dataStruct))
#     sys.stdout.flush()
#   assert 0==1  


  
    
    

# def test_getData():
#   pomodorro.getD
  
  
  
  
  
  
