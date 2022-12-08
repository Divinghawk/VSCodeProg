# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:08:29 2019

@author: Axel
"""

from selenium import webdriver
d = webdriver.Chrome("C:/Data/Applications/chromedriver_win32_v/chromedriver.exe")
url = ''
d.get(url)
d.implicitly_wait(5)
result = d.find_element_by_xpath('')
result.get_attribute('outerHTML')