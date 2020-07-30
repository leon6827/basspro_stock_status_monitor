from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import os

DRIVER_PATH = '../../chromedriver'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

while True:

    print('=== Winchester .40 SW ===')
    driver.get('https://www.basspro.com/shop/en/winchester-usa-handgun-ammo')
    try:
        usa40sw = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345616717636_table')
    except NoSuchElementException:
        usa40sw = None

    try:
        usa40swvp = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_89631_table')
    except NoSuchElementException:
        usa40swvp = None

    try:
        q4238 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_76220_table')
    except NoSuchElementException:
        q4238 = None

    try:
        ww40b = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345617440160_table')
    except NoSuchElementException:
        ww40b = None

    if usa40sw != None:
        print('usa40sw: ' + usa40sw.text + ' [' + str(usa40sw.is_displayed()) + ']')

    if usa40swvp != None:
        print('usa40swvp: ' + usa40swvp.text + ' [' + str(usa40swvp.is_displayed()) + ']')

    if q4238 != None:
        print('q4238: ' + q4238.text + ' [' + str(q4238.is_displayed()) + ']')

    if ww40b != None:
        print('ww40b: ' + ww40b.text + ' [' + str(ww40b.is_displayed()) + ']')

    if usa40sw.is_displayed() or usa40swvp.is_displayed() or q4238.is_displayed() or ww40b.is_displayed():
        os.system('say "Winchester found"')

    print('=== AE .40 SW ===')
    driver.get('https://www.basspro.com/shop/en/federal-american-eagle-centerfire-handgun-ammo')
    try:
        ae40r1 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_131832_table')
    except NoSuchElementException:
        ae40r1 = None

    try:
        ae40r3 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345616700133_table')
    except NoSuchElementException:
        ae40r3 = None

    if ae40r1 != None:
        print('ae40r1: ' + ae40r1.text + ' [' + str(ae40r1.is_displayed()) + ']')

    if ae40r3 != None:
        print('ae40r3: ' + ae40r3.text + ' [' + str(ae40r3.is_displayed()) + ']')

    if ae40r1.is_displayed() or ae40r3.is_displayed():
        os.system('say "American Eagle found"')

    print('=== Blazer .40 SW ===')
    driver.get('https://www.basspro.com/shop/en/blazer-brass-handgun-ammo')

    try:
        blazer5220 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345616736952_table')
    except NoSuchElementException:
        blazer5220 = None

    if blazer5220 != None:
        print('5220: ' + blazer5220.text + ' [' + str(blazer5220.is_displayed()) + ']')

    if blazer5220.is_displayed():
        os.system('say "Blazer found"')

    driver.get('https://www.basspro.com/shop/en/450-406-100122828')
    print('=== Sig Sauer .40 SW ===')

    try:
        e40sb2_200 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345618731665_table')
    except NoSuchElementException:
        e40sb2_200 = None

    if e40sb2_200 != None:
        print('e40sb2-200: ' + e40sb2_200.text + ' [' + str(e40sb2_200.is_displayed()) + ']')

    if e40sb2_200.is_displayed():
        os.system('say "Sig Sauer found"')

    # wait for 5min for the next check
    time.sleep(300)


driver.quit()
