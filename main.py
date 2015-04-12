from pomodorro import *
if __name__ == "__main__":
  while True:
    dataStruct = get_data()
    tick(dataStruct)
    sys.stdout.write(UI(dataStruct))
    set_data(dataStruct)
    del dataStruct
    clearSTDOut()
    time.sleep(ONE_SECOND)
