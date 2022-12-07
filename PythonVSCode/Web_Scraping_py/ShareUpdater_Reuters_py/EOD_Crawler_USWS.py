# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

exchange_list = ['AMEX','FOREX','INDEX','NASDAQ','NYSE','OTCBB']

d = webdriver.Chrome("C:/Data/Applications/chromedriver_win32_v/chromedriver.exe")
#d.implicitly_wait(30)
d.get('http://eoddata.com/download.aspx')
d.find_element_by_id('cboxClose').click()
d.find_element_by_id('ctl00_cph1_ls1_txtEmail').send_keys('axel.hochstein@gmail.com')
d.find_element_by_id('ctl00_cph1_ls1_txtPassword').send_keys('hochstein')
time.sleep(2)
d.find_element_by_id('ctl00_cph1_ls1_btnLogin').click()
time.sleep(5)
d.get('http://eoddata.com/download.aspx')
d.find_element_by_id('ctl00_cph1_d1_cboExchange').click()
for x in exchange_list:
    select = Select(d.find_element_by_id('ctl00_cph1_d1_cboExchange')) 
    select.select_by_value(x)
    d.find_element_by_id('ctl00_cph1_d1_btnDownload').click()
    time.sleep(2)
d.quit()

#Hovering
#element = d.find_element_by_id('ctl00_cph1_d1_btnDownload')
#from selenium.webdriver.common.action_chains import ActionChains
#ActionChains(d).move_to_element(element).perform()
