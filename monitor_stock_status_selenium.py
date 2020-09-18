# README
# 1. set up the DRIVER_PATH after downloading chromedriver for your platform
#    https://chromedriver.chromium.org/
# 2. set up gmail user name and password (SMTP server default to gmail currently)
# 3. run the script

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import smtplib
from smtplib import *
import time
import os

DRIVER_PATH = '../../chromedriver'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

winchester_40sw_stock_prev = False
winchester_9mm_stock_prev = False
winchester_range_40sw_stock_prev = False
winchester_bulk_40sw_stock_prev = False
winchester_bulk_9mm_stock_prev = False
ae_40sw_stock_prev = False
ae_9mm_stock_prev = False
blazer_40sw_stock_prev = False
blazer_9mm_stock_prev = False
sig_40sw_stock_prev = False
sig_9mm_stock_prev = False
herters_9mm_stock_prev = False
 
#set up email
gmail_user = "XXX@gmail.com"
gmail_password = "XXX"

sent_from = gmail_user
to = "YYY@ZZZ.com"
subject = "Bass Pro inventory updated"
body = ""

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
        print('usa40sw: ' + usa40sw.text + ' [' + str(usa40sw.is_displayed()) + ']')
        winchester_40sw_stock |= usa40sw.is_displayed()

    if usa40swvp != None:
        print('usa40swvp: ' + usa40swvp.text + ' [' + str(usa40swvp.is_displayed()) + ']')
        winchester_40sw_stock |= usa40swvp.is_displayed()

    if q4238 != None:
        print('q4238: ' + q4238.text + ' [' + str(q4238.is_displayed()) + ']')
        winchester_40sw_stock |= q4238.is_displayed()

    if winchester_40sw_stock and not(winchester_40sw_stock_prev):
        os.system('say "Winchester 40 found"')
        body += "Winchester 40 found \n"

    winchester_9mm_stock = False
    try:
        q4172 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_73894_table')
    except NoSuchElementException:
        q4172 = None

    if q4172 != None:
        print('q4172: ' + q4172.text + ' [' + str(q4172.is_displayed()) + ']')
        winchester_9mm_stock |= q4172.is_displayed()

    if winchester_9mm_stock and not(winchester_9mm_stock_prev):
        os.system('say "Winchester 9 found"')
        body += "Winchester 9 found \n"

    driver.get('https://www.basspro.com/shop/en/winchester-usa-handgun-ammo-range-pack')
    winchester_range_40sw_stock = False
    try:
        usa40w = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_236459_table')
    except NoSuchElementException:
        usa40w = None

    if usa40w != None:
        print('usa40w: ' + usa40w.text + ' [' + str(usa40w.is_displayed()) + ']')
        winchester_range_40sw_stock |= usa40w.is_displayed()

    if winchester_range_40sw_stock and not(winchester_range_40sw_stock_prev):
        os.system('say "Winchester Range 40 found"')
        body += "Winchester Range 40 found \n"

    print('=== Winchester bulk pack ===')
    driver.get('https://www.basspro.com/shop/en/winchester-usa-handgun-ammo-bulk-pack')
    winchester_bulk_40sw_stock = False
    try:
        ww40b = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345617440160_table')
    except NoSuchElementException:
        ww40b = None

    if ww40b != None:
        print('ww40b: ' + ww40b.text + ' [' + str(ww40b.is_displayed()) + ']')
        winchester_bulk_40sw_stock |= ww40b.is_displayed()

    if winchester_bulk_40sw_stock and not(winchester_bulk_40sw_stock_prev):
        os.system('say "Winchester Bulk 40 found"')
        body += "Winchester Bulk 40 found \n"

    winchester_bulk_9mm_stock = False
    try:
        ww9b = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345617440159_table')
    except NoSuchElementException:
        ww9b = None

    if ww9b != None:
        print('ww9b: ' + ww9b.text + ' [' + str(ww9b.is_displayed()) + ']')
        winchester_bulk_9mm_stock |= ww9b.is_displayed()

    if winchester_bulk_9mm_stock and not(winchester_bulk_9mm_stock_prev):
        os.system('say "Winchester Bulk 9 found"')
        body += "Winchester Bulk 9 found \n"

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
        print('ae40r1: ' + ae40r1.text + ' [' + str(ae40r1.is_displayed()) + ']')
        ae_40sw_stock |= ae40r1.is_displayed()

    if ae40r3 != None:
        print('ae40r3: ' + ae40r3.text + ' [' + str(ae40r3.is_displayed()) + ']')
        ae_40sw_stock |= ae40r3.is_displayed()

    if ae_40sw_stock and not(ae_40sw_stock_prev):
        os.system('say "American Eagle 40 found"')
        body += "American Eagle 40 found \n"

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
        print('ae9dp: ' + ae9dp.text + ' [' + str(ae9dp.is_displayed()) + ']')
        ae_9mm_stock |= ae9dp.is_displayed()

    if ae9fp != None:
        print('ae9fp: ' + ae9fp.text + ' [' + str(ae9fp.is_displayed()) + ']')
        ae_9mm_stock |= ae9fp.is_displayed()

    if ae9dp100 != None:
        print('ae9dp100: ' + ae9dp100.text + ' [' + str(ae9dp100.is_displayed()) + ']')
        ae_9mm_stock |= ae9dp100.is_displayed()

    if ae_9mm_stock and not(ae_9mm_stock_prev):
        os.system('say "American Eagle 9 found"')
        body += "American Eagle 9 found \n"

    print('=== Blazer .40 SW & 9mm ===')
    driver.get('https://www.basspro.com/shop/en/blazer-brass-handgun-ammo')

    blazer_40sw_stock = False
    try:
        blazer5220 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345616736952_table')
    except NoSuchElementException:
        blazer5220 = None

    if blazer5220 != None:
        print('5220: ' + blazer5220.text + ' [' + str(blazer5220.is_displayed()) + ']')
        blazer_40sw_stock |= blazer5220.is_displayed()

    if blazer_40sw_stock and not(blazer_40sw_stock_prev):
        os.system('say "Blazer 40 found"')
        body += "Blazer 40 found \n"

    blazer_9mm_stock = False
    try:
        blazer5201 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345616736948_table')
    except NoSuchElementException:
        blazer5201 = None

    if blazer5201 != None:
        print('5201: ' + blazer5201.text + ' [' + str(blazer5201.is_displayed()) + ']')
        blazer_9mm_stock |= blazer5201.is_displayed()

    if blazer_9mm_stock and not (blazer_9mm_stock_prev):
        os.system('say "Blazer 9 found"')
        body += "Blazer 9 found \n"

    driver.get('https://www.basspro.com/shop/en/450-406-100122828')
    print('=== Sig Sauer Elite .40 SW ===')

    sig_40sw_stock = False
    try:
        e40sb2_200 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345618731665_table')
    except NoSuchElementException:
        e40sb2_200 = None

    if e40sb2_200 != None:
        print('e40sb2-200: ' + e40sb2_200.text + ' [' + str(e40sb2_200.is_displayed()) + ']')
        sig_40sw_stock |= e40sb2_200.is_displayed()

    if sig_40sw_stock and not(sig_40sw_stock_prev):
        os.system('say "Sig Sauer 40 found"')
        body += "Sig Sauer 40 found \n"

    driver.get('https://www.basspro.com/shop/en/sig-sauer-elite-performance-fmj-handgun-ammo')
    print('=== Sig Sauer Elite 9mm ===')

    sig_9mm_stock = False
    try:
        e9mmb2_50 = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345618730635_table')
    except NoSuchElementException:
        e9mmb2_50 = None

    if e9mmb2_50 != None:
        print('e9mmb2-50: ' + e9mmb2_50.text + ' [' + str(e9mmb2_50.is_displayed()) + ']')
        sig_9mm_stock |= e9mmb2_50.is_displayed()

    if sig_9mm_stock and not(sig_9mm_stock_prev):
        os.system('say "Sig Sauer 9mm found"')
        body += "Sig Sauer 9mm found \n"

    driver.get('https://www.basspro.com/shop/en/herters-target-handgun-ammo')
    print('=== Herters 9mm ===')

    herters_9mm_stock = False
    try:
        hrt9a = driver.find_element_by_id('SKU_List_Widget_Add2CartButton_3074457345618973127_table')
    except NoSuchElementException:
        hrt9a = None

    if hrt9a != None:
        print('hrt9a: ' + hrt9a.text + ' [' + str(hrt9a.is_displayed()) + ']')
        herters_9mm_stock |= hrt9a.is_displayed()

    if herters_9mm_stock and not(herters_9mm_stock_prev):
        os.system('say "Herters 9 found"')
        body += "Herters 9 found \n"

    # update flags
    winchester_40sw_stock_prev = winchester_40sw_stock
    winchester_9mm_stock_prev = winchester_9mm_stock
    winchester_range_40sw_stock_prev = winchester_range_40sw_stock
    winchester_bulk_40sw_stock_prev = winchester_bulk_40sw_stock
    winchester_bulk_9mm_stock_prev = winchester_bulk_9mm_stock
    ae_40sw_stock_prev = ae_40sw_stock
    ae_9mm_stock_prev = ae_9mm_stock
    blazer_40sw_stock_prev = blazer_40sw_stock
    blazer_9mm_stock_prev = blazer_9mm_stock
    sig_40sw_stock_prev = sig_40sw_stock
    sig_9mm_stock_prev = sig_9mm_stock
    herters_9mm_stock_prev = herters_9mm_stock

    if body != "":
        email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

            print 'Email sent!'
        except SMTPResponseException as e:
            error_code = e.smtp_code
            error_message = e.smtp_error
            print error_message

    body = ""

    # wait for 5min for the next check
    time.sleep(300)
    print('+++++ 5 min +++++')

driver.quit()
