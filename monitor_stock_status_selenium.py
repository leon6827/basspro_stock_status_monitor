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

    print('=== Winchester .40 SW & 9mm ===')
    driver.get('https://www.basspro.com/shop/en/winchester-usa-handgun-ammo')
    winchester_40sw_stock = False
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

    if usa40sw != None:
        winchester_40sw_stock = usa40sw.is_displayed()
        print('usa40sw: ' + usa40sw.text + ' [' + str(usa40sw.is_displayed()) + ']')

    if usa40swvp != None:
        winchester_40sw_stock = usa40swvp.is_displayed()
        print('usa40swvp: ' + usa40swvp.text + ' [' + str(usa40swvp.is_displayed()) + ']')

    if q4238 != None:
        winchester_40sw_stock = q4238.is_displayed()
        print('q4238: ' + q4238.text + ' [' + str(q4238.is_displayed()) + ']')

    if winchester_40sw_stock:
        os.system('say "Winchester 40 found"')

    winchester_9mm_stock = False
    try:
        q4172 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_73894_table')
    except NoSuchElementException:
        q4172 = None

    if q4172 != None:
        winchester_9mm_stock = q4172.is_displayed()
        print('q4172: ' + q4172.text + ' [' + str(q4172.is_displayed()) + ']')

    if winchester_9mm_stock:
        os.system('say "Winchester 9 found"')

    driver.get('https://www.basspro.com/shop/en/winchester-usa-handgun-ammo-range-pack')
    winchester_range_40sw_stock = False
    try:
        usa40w = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_236459_table')
    except NoSuchElementException:
        usa40w = None

    if usa40w != None:
        winchester_range_40sw_stock = usa40w.is_displayed()
        print('usa40w: ' + usa40w.text + ' [' + str(usa40w.is_displayed()) + ']')

    if winchester_range_40sw_stock:
        os.system('say "Winchester Range 40 found"')

    driver.get('https://www.basspro.com/shop/en/winchester-usa-handgun-ammo-bulk-pack')
    winchester_bulk_40sw_stock = False
    try:
        ww40b = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345617440160_table')
    except NoSuchElementException:
        ww40b = None

    if ww40b != None:
        winchester_bulk_40sw_stock = ww40b.is_displayed()
        print('ww40b: ' + ww40b.text + ' [' + str(ww40b.is_displayed()) + ']')

    if winchester_bulk_40sw_stock:
        os.system('say "Winchester Bulk 40 found"')

    winchester_bulk_9mm_stock = False
    try:
        ww9b = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345617440159_table')
    except NoSuchElementException:
        ww9b = None

    if ww9b != None:
        winchester_bulk_9mm_stock = ww9b.is_displayed()
        print('ww9b: ' + ww9b.text + ' [' + str(ww9b.is_displayed()) + ']')

    if winchester_bulk_9mm_stock:
        os.system('say "Winchester Bulk 9 found"')

    print('=== AE .40 SW & 9mm ===')
    driver.get('https://www.basspro.com/shop/en/federal-american-eagle-centerfire-handgun-ammo')
    ae_40sw_stock = False
    try:
        ae40r1 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_131832_table')
    except NoSuchElementException:
        ae40r1 = None

    try:
        ae40r3 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345616700133_table')
    except NoSuchElementException:
        ae40r3 = None

    if ae40r1 != None:
        ae_40sw_stock = ae40r1.is_displayed()
        print('ae40r1: ' + ae40r1.text + ' [' + str(ae40r1.is_displayed()) + ']')

    if ae40r3 != None:
        ae_40sw_stock = ae40r3.is_displayed()
        print('ae40r3: ' + ae40r3.text + ' [' + str(ae40r3.is_displayed()) + ']')

    if ae_40sw_stock:
        os.system('say "American Eagle 40 found"')

    ae_9mm_stock = False
    try:
        ae9dp = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_131828_table')
    except NoSuchElementException:
        ae9dp = None

    try:
        ae9fp = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345616700134_table')
    except NoSuchElementException:
        ae9fp = None

    try:
        ae9dp100 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345616932618_table')
    except NoSuchElementException:
        ae9dp100 = None

    if ae9dp != None:
        ae_9mm_stock = ae9dp.is_displayed()
        print('ae9dp: ' + ae9dp.text + ' [' + str(ae9dp.is_displayed()) + ']')

    if ae9fp != None:
        ae_9mm_stock = ae9fp.is_displayed()
        print('ae9fp: ' + ae9fp.text + ' [' + str(ae9fp.is_displayed()) + ']')

    if ae9dp100 != None:
        ae_9mm_stock = ae9dp100.is_displayed()
        print('ae9dp100: ' + ae9dp100.text + ' [' + str(ae9dp100.is_displayed()) + ']')

    if ae_9mm_stock:
        os.system('say "American Eagle 9 found"')

    print('=== Blazer .40 SW & 9mm ===')
    driver.get('https://www.basspro.com/shop/en/blazer-brass-handgun-ammo')

    blazer_40sw_stock = False
    try:
        blazer5220 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345616736952_table')
    except NoSuchElementException:
        blazer5220 = None

    if blazer5220 != None:
        blazer_40sw_stock = blazer5220.is_displayed()
        print('5220: ' + blazer5220.text + ' [' + str(blazer5220.is_displayed()) + ']')

    if blazer_40sw_stock:
        os.system('say "Blazer 40 found"')

    blazer_9mm_stock = False
    try:
        blazer5201 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345616736948_table')
    except NoSuchElementException:
        blazer5201 = None

    if blazer5201 != None:
        blazer_9mm_stock = blazer5201.is_displayed()
        print('5201: ' + blazer5201.text + ' [' + str(blazer5201.is_displayed()) + ']')

    if blazer_9mm_stock:
        os.system('say "Blazer 9 found"')

    driver.get('https://www.basspro.com/shop/en/450-406-100122828')
    print('=== Sig Sauer .40 SW ===')

    sig_40sw_stock = False
    try:
        e40sb2_200 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345618731665_table')
    except NoSuchElementException:
        e40sb2_200 = None

    if e40sb2_200 != None:
        sig_40sw_stock = e40sb2_200.is_displayed()
        print('e40sb2-200: ' + e40sb2_200.text + ' [' + str(e40sb2_200.is_displayed()) + ']')

    if sig_40sw_stock:
        os.system('say "Sig Sauer 40 found"')

    driver.get('https://www.basspro.com/shop/en/herters-target-handgun-ammo')
    print('=== Herters 9mm ===')

    herters_9mm_stock = False
    try:
        hrt9a = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345618973127_table')
    except NoSuchElementException:
        hrt9a = None

    if hrt9a != None:
        herters_9mm_stock = hrt9a.is_displayed()
        print('hrt9a: ' + hrt9a.text + ' [' + str(hrt9a.is_displayed()) + ']')

    if herters_9mm_stock:
        os.system('say "Herters 9 found"')

    # wait for 5min for the next check
    time.sleep(300)
    print('+++++ 5 min +++++')

driver.quit()
