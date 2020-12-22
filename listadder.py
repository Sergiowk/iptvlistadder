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





num_lines = sum(1 for line in open('.\playlists.txt'))
print ("Lines in total: %s" % (num_lines))

#Open the playlists file
f = open('.\playlists.txt', "r")

line = f.readline()
countname = 1
while line:
    #Getting the values from the web
    macAdress = driver.find_element_by_name('TxtMacAddress')
    playlistName = driver.find_element_by_name('TxtName')
    playlistLink = driver.find_element_by_name('TxtLink')
    
    
    print(line)
    print(countname)
    # use realine() to read next line
    line = f.readline()
    
    #
    link = line
    name = countname
    #Introducing the values on the web
    print (countname)
    print (link)
    macAdress.send_keys(mac)
    playlistName.send_keys(name)
    playlistLink.send_keys(link)
    #Saving
    saveList = driver.find_element_by_name('CmdSave')
    sleep(2)
    saveList.click()
    #Letting the web loading
    sleep(5)
    countname = countname + 1
f.close()
