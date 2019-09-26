from selenium import webdriver
from PySelenium_Test_Modul import *

'''
Yandex search
'''

browser_test = test_class('http://yandex.ru', webdriver.Chrome())
browser_test.text_to_searchTab('//input[@name="text"]','python', 'popup__content')
browser_test.link_search('https://tensor.ru', '//*[@class="serp-item"]//h2//a', '//h2//a', 5)
browser_test.quit()

'''
Pictures on Yandex
'''

browser_test = test_class('http://yandex.ru', webdriver.Chrome())
browser_test.click_system(1, '//*[@href="//yandex.ru/images/"]')
browser_test.url_equal_link('https://www.python.org/')
browser_test.click_system(0, 'cl-teaser__link')
browser_test.image('img')
browser_test.image_check(False, 'img')
browser_test.click_system(0, 'cl-layout__nav__right')
browser_test.image('img')
browser_test.click_system(0, 'cl-layout__nav__left')
browser_test.image('img')
browser_test.image_check(True, 'img')
browser_test.quit()


