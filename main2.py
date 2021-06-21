import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
links = [ 
    "https://www.linkedin.com/mynetwork/invitation-manager/"
    ]

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options);
driver.get("https://linkedin.com")



while input("Press 1 when signed in ") != "1":
    pass

for link in links:
    try:
        for i in range(1):

            print("Accessing Link: ", link)
            driver.get(link)
            sleep(3)
            XPath = "/html/body/div[6]/div[3]/div/div/div/div/div/div/div/main/section/div[2]/section/div/ul/li[1]/div[1]/div[2]/button[2]"
            elem = driver.find_element_by_xpath(XPath)

            print("Accepting request")

            elem.click()
            driver.get(link)
            print("Accepted!")
            sleep(5)
        
    except Exception as e:
        print("Error processing link\nlink: ", link, "\nerror", e)

driver.close()
