"""
chrome_test.py
"""

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

driver = webdriver.Chrome(chrome_options = chrome_options)

driver.get('https://github.com/gingeleski')

print(driver.page_source)

driver.quit()
