from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

def initialize():
    #Driver initialization
    driver = webdriver.Chrome(".\chromedriver.exe")
    driver.get("https://iptvextreme.eu/") 
    #Letting the web loading
    sleep(2)
    return driver

def insertlist(driver):
    num_lines = sum(1 for line in open('.\playlists.txt'))
    print ("Playlists: %s" % (num_lines-1))
    
    
    
    macsGets = gettingmacs()
    for mac in macsGets: 
        print (mac)
        driver.get("https://iptvextreme.eu/") 
        countname = 1
        #Letting the web loading
        sleep(2)
        #Open the playlists file
        fo = open('.\playlists.txt', "r")
        line = fo.readline()
        while line:
            #Getting the values from the web
            macAdress = driver.find_element_by_name('TxtMacAddress')
            macAdress.send_keys(mac)
            playlistName = driver.find_element_by_name('TxtName')
            playlistLink = driver.find_element_by_name('TxtLink')
            
            
            
            # use realine() to read next line
            line = fo.readline()

            
            
            link = line
            name = countname
            

            #Introducing the values on the web
            print (countname)
            print (link)

            print("Link: %s" % link)
            print("Mac: %s" % mac)
            print("Name: %s" % name)

            
            playlistName.send_keys(name)
            playlistLink.send_keys(link)
            sleep(1)
            #Saving
            saveList = driver.find_element_by_name('CmdSave')
            
            saveList.click()
            
            #Letting the web loading
            sleep(2)
            countname = countname + 1
    fo.close()

def gettingmacs():
    num_lines = sum(1 for line in open('.\macslist.txt'))
    print ("Macs: %s" % (num_lines-1))
    mac = []
    #Open the playlists file
    f = open('.\macslist.txt', "r")

    line = f.readline()

    while line:
        print(line)

        # use realine() to read next line
        line = f.readline()
        mac.append(line)
    f.close()

    return mac