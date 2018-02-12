# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:33:05 2018

@author: ryan-kuhl
"""
from bs4 import BeautifulSoup
import requests
import time
from tkinter import messagebox
def getbutton():
  page = requests.get('https://www.andersonmanufacturing.com/product/lower-parts-kit-minus-pistol-grip/')
  soup = BeautifulSoup(page.text, 'lxml')
  links = soup.find('p', {'class' : 'out-of-stock'})
  
  if links:
    print('ya')
    time.sleep(30)
  else:
    b = messagebox.showinfo("OBDM Alpha One Command Center","Anderson\n BUY BUY BUY BUY BUY BUY")
while __name__ == '__main__':
  
  getbutton() 
 
