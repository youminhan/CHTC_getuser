
import os,sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv
number = int(sys.argv[1])
number = number + 1
writeFile = open('result.csv', 'w')
namelist = []
projectlist = []
timelist = []
userlist = []
emaillist1= []
emaillist2= []
userlist = []
#Open website and login
dir,file = os.path.split(os.path.abspath(sys.argv[0]))
browser = webdriver.Chrome(dir + '/chromedriver')
browser.get('https://wwwapps.chtc.wisc.edu//chtcuser/')
username = browser.find_element_by_id("username-input")

# Enter your user name here
username.send_keys("username")
password = browser.find_element_by_id("password-input")

# Enter your password here
password.send_keys("password")
browser.find_element_by_css_selector('input.btn.btn-primary.btn-large').click()


# for row in table.find_elements_by_xpath(".//tr"):
  
for x in range(1, number, 1):
    browser.find_element_by_id('user-btn').click()
    table =  browser.find_element_by_id('list-table')
    path2 = '//tbody/tr[' + str(x) +']/td[8]'
    time = table.find_element_by_xpath(path2)
    timelist.append(time.text)
    path4 = '//tbody/tr[' + str(x) +']/td[1]'
    user = table.find_element_by_xpath(path4)
    userlist.append(user.text)

    path3 = '//tbody/tr[' + str(x) +']/td[1]'
    user = table.find_element_by_xpath(path3)
    user.click()
    
    
    
    name = browser.find_element_by_id('name-input')
    namelist.append(name.get_attribute("value"))
    
    email1 = browser.find_element_by_id('email1-input')
    emaillist1.append(email1.get_attribute("value"))
    
    email2 = browser.find_element_by_id('email2-input')
    emaillist2.append(email2.get_attribute("value"))
    
    select = browser.find_element_by_id('primary-proj-select')
    selected_option = select.find_element_by_xpath('.//option[2]')
    projectlist.append(selected_option.text)


writeFile.write("Username,"+"Name," + "Email1," + "Email2,"+"Projects,"  + "Time\n")
for x in range(1, number, 1):
   writeFile.write(userlist[x-1] +"," +namelist[x-1]  +"," + emaillist1[x-1]+ "," + emaillist2[x-1]+ ","+ projectlist[x-1] + ","+ timelist[x-1] + "\n" )

browser.close()
        
