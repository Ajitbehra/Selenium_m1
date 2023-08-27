#8.xpath

#path of an element present in html tree structure is called as xpath.
# *xpath is classified into 2 types,
 # 1.absolute xpath
 # 2.relative xpath

# 1.absolute xpath:
 # *****************
 # *absolute xpath indicate by "single forward slash(/)".
 # *"/" --> traverse from parent to immediate child.
 #
 # drawback of absolute xpath:
 # ===========================
 # *xpath will be lengthly compratively relative xpath.
 # *always we should traverse from parent to immediate child only.
 # *to over come this drawback we go relative xpath

# 2.relative xpath:
 # *****************
 # *relative xpath indicates by "double forward slash(//)".
 # *"//" --> traverse from parent to any of its child.


 ##############################################################################################################
from selenium.webdriver import Chrome
from time import sleep


#xpath by attribute:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.ksrtc.in/oprs-web/")
# driver.find_element("xpath","//a[@title = 'Recruitment']").click()

#xpath by group by indexing:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.ksrtc.in/oprs-web/")
# driver.find_element("xpath","//a[@class = 'nav-link' and @title='Recruitment']").click()

#xpath with multiple attiributes:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.ksrtc.in/oprs-web/")
# driver.find_element("xpath","(//a[@class = 'nav-link'])[5]").click()

# xpath to inspect leaving from to heading to in ksrtc:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.ksrtc.in/oprs-web/")
# driver.find_element("xpath","//input[@name='txtReturnJourneyDate']")
# driver.find_element("xpath","//input[@name='toPlaceName']")

#xpath to inspect sunglasses in lenskart:
#here class attribute is matching with multiple elements so that we can use these methods:
#1 xpath with multiple attributes:
#
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.lenskart.com/")
# sleep(3)
# driver.find_element("xpath","//a[@class= 'LastRowLink--1klhk6r jpBosF getGaData' and @id='lrd2']").click()

#xpath by group by indexing:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.lenskart.com/")
# driver.find_element("xpath","(//a[@class = 'LastRowLink--1klhk6r jpBosF getGaData'])[2]").click()



# #19-8-23     Assignment:
#
# #ws to launch passport seva application :
#
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.passportindia.gov.in/AppOnlineProject/welcomeLink#")
# driver.maximize_window()
# sleep(3)
# driver.find_element("xpath","//div[@class = 'main_button_typ_002']").click()
# driver.find_element("xpath","//label[. = 'Passport Office']").click()
# driver.find_element("xpath","//select[@name='dcdrLocation']").click()
# driver.find_element("xpath","//option[. ='Ahmedabad']").click()
# driver.find_element("xpath","//input[@name='givenName']").send_keys("Ajit kumar")
# driver.find_element("xpath","//input[@name='surname']").send_keys("Behra")
# driver.find_element("xpath","//input[@name='dob']").send_keys("15/04/1995")
# driver.find_element("xpath","//input[@name='email']").send_keys("ajitbehra1996@gmail.com")
# driver.find_element("xpath","//label[ .='Yes']").click()
# driver.find_element("xpath","//input[@name='loginId']").click()
# driver.find_element("xpath","//input[@class='txtbox'])[5]").send_keys("Demo@1901")
# driver.find_element("xpath","//input[@class='txtbox'])[6]").send_keys("Demo@1901")
# driver.find_element("xpath","//select[@name='hintQues']").click()
# driver.find_element("xpath","//option[. ='Favourite Colour']").click()
# driver.find_element("xpath","//input[@name='hintAns']").send_keys("Black")
# driver.find_element("xpath","//input[@name='register']").click()
#
# #ws to launch spotify application:
#
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://open.spotify.com/")
# driver.maximize_window()
# driver.find_element("xpath","//button[. ='Sign up']").click()
# sleep(5)
# driver.find_element("xpath","//input[@id='email']").send_keys("ajitbehra1996@gmail.com")
# driver.find_element("xpath","//input[@name='password']").send_keys("Demo@1996")
# driver.find_element("xpath","//input[@name='displayname']").send_keys("Ajitt")
# driver.find_element("xpath","//input[@name='year']").send_keys("1995")
# driver.find_element("xpath","//select[@name='month']").click()
# driver.find_element("xpath","//option[. ='April']").click()
# driver.find_element("xpath","//input[@name='day']").send_keys("29")
# driver.find_element("xpath","//span[. ='Male']").click()
# driver.find_element("xpath","//span[contains(. ,'I would prefer')]").click()
# driver.find_element("xpath","(//span[contains(. ,'Share my registration')])[2]").click()
# driver.find_element("xpath","//span[. ='Sign up']").click()

#NOTE ---
 #challenges i face during writing script:

 #1 advirtisement popup


#ws to launch zomato:
#
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.zomato.com/india")
# driver.maximize_window()
# driver.find_element('xpath',"//a[. = 'Sign up']").click()
# driver.find_element("xpath","//label[@class ='sc-1yzxt5f-7 fGFJFM']").send_keys('Ajit Behra')

#21-8-23
#xpath by partial dynamic element:

#ws to inspect Higgines wonderpants:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.medplusmart.com/")
# driver.find_element("xpath","//span[contains(. , 'HUGGIES WONDER PANTS')]").click()

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.medplusmart.com/")
# driver.maximize_window()
# driver.find_element("xpath","(//h6[contains(@class, 'truncate-line-2')])[2]").click()

#ws to inspect  shirt in flipkart:
# //a[contains(. , 'Men Regular Fit Checkered Spread Collar Casual Shirt')]

#######################################################################
#22-8-23
#completely dynamic element:


# xpath to inspect no of views in youtube
# xpath to inspect no of likes in youtube
# xpath to inspect no of subscribes in youtube
# xpath to inspect price of shirt in amazon
# xpath to inspect offer of any product mamaeart
# xpath to find % of 5* in pharmacy
# (https://pharmeasy.in/health-care/products/venusia-max-intensive-moisturizing-cream-for-dry-very-dry-skin-tube-of-150-g-8293)
# xpath to find birt in this year
# (https://www.worldometers.info/)


#xpath to inspect rating of jailer movie:
# //td[. = 'JAILER']/../td[4]

#xpath to inspect box ofice collections of 3 idiots movie:
# //td[. = '3 IDIOTS']/../td[3]

#xpath to inspect revie of movie:
# //td[. ='GADAR 2']/..//td[5]

#xpath to inspect ratings of Gadar 2 movie:
# //h1[contains(. ,'Gadar 2:')]/../section/div/span[1]

# xpath to inspect voting of gadar 2 movie:
# //h1[contains(.,'Gadar 2')]/../section/div/span[2]
#
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://in.bookmyshow.com/mumbai/movies/gadar-2-the-katha-continues/ET00338629")
# driver.maximize_window()
# driver.find_element("xpath","//h1[contains(.,'Gadar 2')]/../section/div/span[2]").click()

#xpath to inspect oppo phone in flipkart:
# (//div[contains(. ,'OPPO F21 Pro 5G (Rainbow')])[12]/../../div/div/div/div[1]
#or (//div[contains(. ,'OPPO F21 Pro 5G (Rainbow')])[12]/../../div[2]/div/div/div

#xpath to inspect orice of nifty 50 in nse:
# //p[. ='NIFTY 50']/../p[2]

#xpath to find birth this year :
# //span[.='Births this year']/../span


#############################################################
#23-8-23  #Handling xpath by sibling function:

#xpath to inspect ratings of movie :
# //td[.='3 IDIOTS']/following-sibling::td[2]

#xpath to inspect revies of  Hera pheri movie:
# //td[.='HERA PHERI']/following-sibling::td[3]

#xpath to inspect Slno of the movie:
# //td[.='GADAR 2']/preceding-sibling::td

#xpath to inspect votes of ghoomer movie in book my show:
# //h1[.='Ghoomer']/../section/div/span

#xpath to inspect rating of jailer movie:
# //h1[.='Jailer']/following-sibling::section/div/span[1]

#xpath to inspect votes of jailer movie:
# //h1[.='Jailer']/following-sibling::section/div/span[2]

#xpath to inspect likes of dreamgirl movie:
# (//h1[.='Dream Girl 2']/../..//span[@class='sc-15uprjp-1 ReIPF'])[2]

#xpath to inspect  births this year:
# //span[.='Births this year']/../span/span
# //span[.='Births this year']/preceding-sibling::span/span


#xpath to inspect offer of any product mamasearth:
# (//div[contains(.,'Onion Shampoo with Onion & Plant Keratin for Hair Fall')])[16]/following-sibling::div/div[3]


# xpath to find % of 5* in pharmacy
# //div[.='Ratings and Reviews']/../div[2]/div[2]/div[1]/div[3]


#xpath to inspect review of the center court goa hotel:
# (//div[.='The Center Court Goa'])[2]/../../../div[3]/div[3]/div/div
# (//div[.='The Center Court Goa'])[2]/../../following-sibling::div/div[3]/div/div[1]


#ancester function:
#/amcestor::tagname

#xpath to inspect whole body:
# //td[.='BATMAN ']/ancestor::body

#xpath to inspect html page:
# //td[.='MISSION IMPOSSIBLE ']/ancestor::html