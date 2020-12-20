from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#Driver initialization
driver = webdriver.Chrome(".\chromedriver.exe")
driver.get("https://iptvextreme.eu/") 
#Letting the web loading
sleep(5)

#Variables initialization
mac = "MAC ADRESS"
name = "Name"
link = "www.iptvlist.com"

#Getting the values from the web
macAdress = driver.find_element_by_name('TxtMacAddress')
playlistName = driver.find_element_by_name('TxtName')
playlistLink = driver.find_element_by_name('TxtLink')
saveList = driver.find_element_by_name('CmdSave')
#elem.clear()

#Introducing the values on the web
macAdress.send_keys(mac)
playlistName.send_keys(name)
playlistLink.send_keys(link)
#Saving
saveList.click()
#Letting the web loading
sleep(5)


