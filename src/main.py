import time
import pyautogui as gui

gui.press("win")
gui.write("edge")
gui.press("enter")

time.sleep(3)

gui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
gui.press("enter")
time.sleep(3)
