import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install());
driver.get("https://linkedin.com")


links = [
        "https://www.linkedin.com/posts/kushagratandon124_machinelearning-artificialintelligence-deeplearning-activity-6800986275684986881-Wpoo"
]

while input("Press 1 when signed in ") != "1":
    pass

for link in links:
    try:
        print("Accessing Link: ", link)
        driver.get(link)
        sleep(3)
        elem = driver.find_element_by_class_name("react-button__trigger")

        if elem.get_attribute("aria-pressed") == "false":
            print("Liking the post")
            elem.click()
            print("Liked")
            sleep(2)
        else:
            print("Already Liked")
    except Exception as e:
        print("Error processing link\nlink: ", link, "\nerror", e)

driver.close()
