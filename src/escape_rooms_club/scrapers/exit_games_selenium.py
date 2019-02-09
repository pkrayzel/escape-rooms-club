from selenium import webdriver
import time

#
# url = "https://www.exitgames.cz/Seznam-unikovych-her"
# browser = webdriver.Chrome("/usr/local/bin/chromedriver")
# browser.get(url)
# html = browser.page_source.encode('utf-8')
# page_num = 0
#
# while browser.find_elements_by_css_selector('#next_products'):
#     browser.find_element_by_css_selector('#next_products').click()
#     page_num += 1
#     print("getting page number "+str(page_num))
#     time.sleep(1)
#     print(browser.page_source.encode('utf-8'))
#
# html = browser.page_source.encode('utf-8')
#
# print(html)
from selenium import webdriver
import time


def store_file(page_num, driver):
    file_ = open(f"output_{page_num}.txt", "w")
    file_.write(driver.page_source)
    file_.close()


url = "https://www.exitgames.cz/Seznam-unikovych-her"
driver = webdriver.PhantomJS()

try:
    driver.get(url)
    html = driver.page_source.encode('utf-8')
    page_num = 0

    while driver.find_elements_by_css_selector('#next_products'):
        driver.find_element_by_css_selector('#next_products').click()
        page_num += 1
        print("getting page number "+str(page_num))
        store_file(page_num, driver)
        time.sleep(1)

    html = driver.page_source.encode('utf-8')

except Exception as e:
    driver.save_screenshot(f'{page_num}.png')
    store_file(page_num, driver)

driver.close()