import pyautogui
from PIL import ImageGrab
import numpy as np
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("chrome://dino/")
elem = driver.find_element_by_id('t')
time.sleep(1)
pyautogui.press('space')

x1=325
x2=500
y1=544
y2=596                 

def pixel():
    im = ImageGrab.grab().crop((x1,y1,x2,y2))
    im.save('screenshot.png')
    time.sleep(0.01)
    im_array = np.asarray(im)
    return (im_array)     
                                          
while True:
    arr = pixel()
    if (([83,83,83] or [83,255,255] or
        [255,83,255] or [255,255,83] or
        [83,83,255] or [83,255,83] or
        [255,83,83]) in arr):
        pyautogui.press('space')
    time.sleep(0.01)    