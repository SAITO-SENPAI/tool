from color.color import *
from src.banner import *
from src.selection import *
import time, os
import requests
from datetime import datetime


key=requests.get("https://pastebin.com/raw/0iu0f714").text
time.sleep(0.5)
os.system("clear")
def main():
  while True:
    Key = str(input(f"{g}Your key: "))
    if Key == key:
        os.system("clear")
        bn()
        break
    else:
      print(f"{r}\n\nYou Entered Wrong Key, Please Enter Again!\n\n")
      
      
      
main()
def hub():
  while True:
    sl()
    SL = str(input(f"{c}Enter An Option: "))
    if (SL == "1" or SL == "01"):
      print("Update")
    elif (SL == "2" or SL == "02"):
      os.system("xdg-open https://www.facebook.com/profile.php?id=100020625430658")
    elif (SL == "3" or SL == "03"):
      break
    elif (SL == "4" or SL == "04"):
      s = int(input(f"{c}Countdown Time: "))
      for i in range(s, -1, -1):
        print(f"{r}Countdown: ",i ,end=" \r ")
        time.sleep(1)
      os.system("clear") 
      bn()
    elif (SL == "5" or SL == "05"):
      url = str(input(f"{g}Url: "))
      os.system("xdg-open " + url)
      os.system("clear")
      bn()
    elif (SL == "6" or SL == "06"): 
      while True:
          time=datetime.now().strftime("%H:%M:%S")
          print(f"{r}Time is: ", time, end="\r")
      time.sleep(0.5)
          
    else:
      print(f"\n\n{r}Select 1, 01, 2, 02, 3, 03, 4, 04!")
hub()