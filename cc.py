from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
from getpass import getpass
import time
import sys
from selenium.webdriver.support import expected_conditions as EC

        
options = Options()
options.add_argument("--disable-notifications") 
driver = webdriver.Chrome(r"C:\Users\Shubham\Downloads\chromedriver.exe",chrome_options=options)
driver.get("https://www.codechef.com/rankings/ACMIND18?filterBy=&order=asc&sortBy=rank")
list1=driver.find_elements_by_class_name('institute')
for j in range(0,len(list1)):
    list1[j]=list1[j].text
driver.get("https://www.codechef.com/rankings/ACMIND18?filterBy=&order=asc&page=2&sortBy=rank")
list2=driver.find_elements_by_class_name('institute')
for j in range(0,len(list2)):
    list2[j]=list2[j].text
final=list1+list2
your_rank=910
print(len(set(final[:your_rank])))
    
#f.close()
    
