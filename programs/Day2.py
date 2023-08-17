from selenium.webdriver import Chrome

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://ajio.com")
# driver.maximize_window()


# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# driver.minimize_window()


#
# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# driver.fullscreen_window()


#
#
# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# pos = driver.get_window_position()
# print(pos)
# print(pos['x'])
#
#


# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# size = driver.get_window_size()
# print(size)
# print(f" Height = {size['height']}")
# print(f" Width = {size['width']}")




# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# rect = driver.get_window_rect()
# print(rect)

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# driver.set_window_position(20,100)

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# driver.set_window_size(100,500)


# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# driver.set_window_rect(50,100,400,800)


#verification browser commands:

# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://ajio.com")
# t = driver.title
# print(t)
#
#
# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# t = driver.title
# if t == "Online Shopping for Women, Men, Kids – Clothing, Footwear | AJIO":
#     print("Home page displayed, testcase pass")
# else:
#     print("testcase fail")


# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# url = driver.current_url
# print(url)
#
# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# url = driver.current_url
# if url =="https://www.ajio.com/":
#     print("home page displayed ,test case pass")
# else:
#     print("testcase fail")


#
# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com/shop/men")
# page = driver.page_source
# print(page)
#
#
# driver = Chrome(executable_path=r"../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# page = driver.page_source
# if "Online Shopping for Men - Buy Shirts, T-shirts, Jeans, Trousers, Jackets, Shoes &amp; more." in page:
#     print("content present")
# else:
#     print("defect")


