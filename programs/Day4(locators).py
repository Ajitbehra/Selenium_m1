from selenium.webdriver import Chrome
from time import sleep

#1 example on single matching element:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("file:///C:/Users/HP/Desktop/demoooo.html")
# username = driver.find_element("id","a1")
# username.send_keys("Ajit Behra")


#2 example on multiple matching element:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("file:///C:/Users/HP/Desktop/demoooo.html")
# pwd = driver.find_element("id","a1")
# pwd.send_keys("Ajitbehra@123")

#3 example on no matching element:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("file:///C:/Users/HP/Desktop/demoooo.html")
# pwd = driver.find_element("id","a111")
# pwd.send_keys("Ajitbehra@123")

#write a script to enter username,password in fb:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.fb.com")
# un = driver.find_element("id","email")
# un.send_keys("Ajit behra")
#
# pwd = driver.find_element("id","pass")
# pwd.send_keys("Ajitbehra@123")


#write a script to serach for watch in amazon:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.amazon.com")
# src = driver.find_element("id","twotabsearchtextbox")
# src.send_keys("headphone")
#
# src_btn = driver.find_element("id","nav-search-submit-button")
# src_btn.click()



#day:4
#ws to search for watch in demowebshop.com:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element("name","q").send_keys("watch")

#ws to enter the username in IRCTC:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.irctc.co.in/nget/profile/user-registration")
# driver.maximize_window()
# driver.find_element("name","userName").send_keys("Ajitbehra1995")

#ws to enter rajajinagar loction in swiggy.com:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.swiggy.com/")
# driver.maximize_window()
# driver.find_element("name","location").send_keys("Raigarh")


#Class name:

#ws to click on  Sign up and enter all the details:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.swiggy.com/")
# driver.maximize_window()
# driver.find_element("class name","r2iyh").click()
# driver.find_element("name","mobile").send_keys("8819989319")
# driver.find_element("name","name").send_keys("Ajit")
# driver.find_element("name","email").send_keys("guddubehra1995@gmail.com")
# driver.find_element("class name","a-ayg").click()

#ws to search for goa in flipkart booking:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.flipkart.com/travel/flights")
# sleep(3)
# driver.find_element("class name","_1w3ZZo._1YBGQV._2EjOJB.lZd1T6._2dqBfU._2mFmU7").send_keys("goa")


#ws to cliclk on hotels in make my trip:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.makemytrip.com")
# driver.maximize_window()
# driver.find_element("class name","chNavText.darkGreyText").click()

#Tag name:

#ws to click on movie in book my show:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://in.bookmyshow.com/explore/home/mumbai")
# driver.find_element("tag name","a")

#ws to click on demowebshop:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element("tag name","a").click()

##########################################################################################################

#5  Link text:

#ws to click on facebook link in dummy webpage:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("file:///C:/Users/HP/Desktop/demoooo.html")
# sleep(3)
# driver.find_element("link text","Facebook").click()


#ws to click on best sellers in amazon:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# driver.find_element("link text","Best Sellers").click()

#ws to click on fantasy cricket in dream 11:
#
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.dream11.com/fantasy-cricket")
# driver.find_element("link text","Dream11").click()

#ws to click on travel info and metro timings in bmrcl:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://english.bmrc.co.in/#/")
# driver.maximize_window()
# driver.find_element("link text","TRAVEL INFO").click()
# driver.find_element("link text","Metro Timings").click()
# driver.back()
# driver.find_element("link text","TRAVEL INFO").click()
# driver.find_element("link text","Tickets").click()

#ws to click on whow more and click on onion in bigbasket:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://bigbasket.com/")
# driver.find_element("link text","Show More").click()
# driver.find_element("link text","Farm Eggs - Regular, Medium, Antibiotic Residue-Free").click()

##################################################################################################

#6 Partial link text:
#
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.selenium.dev/downloads/")
# driver.find_element("partial link text","languages").click()

#ws to click on lekme product in lakme:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://lakmeindia.com/")
# driver.maximize_window()
# driver.find_element("partial link text","all products").click()


#assignment:
#ws to click on register and fill all the details and register from demo webshop:
#
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element("link text","Register").click()
# driver.find_element("id","gender-male").click()
# driver.find_element("name","FirstName").send_keys("Ajit")
# driver.find_element("name","LastName").send_keys("Behra")
# driver.find_element("name","Email").send_keys("Ajitbehra1995@gmail.com")
# driver.find_element("name","Password").send_keys("demo@1995")
# driver.find_element("name","ConfirmPassword").send_keys("demo@1995")
# driver.find_element("id","register-button").click()

######################################################################################

#CSS SELECTOR:

#ws to search for chiceken and click on the first link:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.licious.in/search")
# driver.maximize_window()
# driver.find_element("css selector","input[class = 'RealSearchBar_searchbar__zap4G']").send_keys("chicken")
# driver.find_element("css selector","div[class='SearchProductTile_item_description__e3i11']").click()3


#ws to automate on dunzo:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.dunzo.com/bangalore")
# driver.maximize_window()
# driver.find_element("css selector","button[data-tip='header-business-options']").click()
# driver.find_element("css selector","div[class='sc-AxjAm StDqM sc-jbkzle-4 PCMWw']").click()
# driver.find_element("css selector","input[name = 'phone']").send_keys("8819989319")
# driver.find_element("css selector","input[name = 'emailID']").send_keys("ajitbehra1996@gmail.com")
# driver.find_element("css selector","input[name = 'password']").send_keys("ajitbehra1995@")
# driver.find_element("css selector","svg[class = 'sc-Axmtr osNtE sc-fznyAO gTtLDV']").click()
# driver.find_element("css selector","button[class = 'sc-AxiKw KKPII sc-1q182yc-4 hpwiSq']").click()


#ws to search for a song and click on play in youtube:

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.youtube.com/")
# driver.find_element("css selector","input[id ='search']").send_keys("Heeriye")
# driver.find_element("id","search-icon-legacy").click()
# driver.find_element("css selector","yt-formatted-string[class='style-scope ytd-video-renderer']").click()