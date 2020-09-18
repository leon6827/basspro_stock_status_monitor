# README
# 1. set up the DRIVER_PATH after downloading chromedriver for your platform
#    https://chromedriver.chromium.org/
# 2. set up gmail user name and password (SMTP server default to gmail currently)
#    gmail might block your login using non-Google app, please check your gmail security setting
# 3. run the script

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import smtplib
from smtplib import *
import time
import os
import simplejson as json

#set up webdriver
DRIVER_PATH = '../../chromedriver'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#read inventory url list
with open('./inventory.json') as f:
    json_data = json.load(f)

#set up gmail
gmail_user = "XXX@gmail.com"
gmail_password = "XXX"

sent_from = gmail_user
to = "YYY@ZZZ.com"
subject = "Bass Pro inventory updated"
email_body = ""

#main processing loop
while json_data != None:
    print(json_data["inventory_urls"])

    for url in json_data["inventory_urls"]:
        print('=== ' + url["name"] + ' ===')
        driver.get(url["url"])
        time.sleep(5)

        url["curr_instock"] = False
        for item in url["items"]:
            try:
                web_element = driver.find_element_by_id(item["sku"])
            except NoSuchElementException:
                web_element = None

            if web_element != None:
                print(item["model"] + ': ' + web_element.text + ' [' + str(web_element.is_displayed()) + ']')
                url["curr_instock"] |= web_element.is_displayed()

        if url["curr_instock"] and not(url["prev_instock"]):
            os.system('say ' + url["name"])
            email_body += url["name"] + 'found \n'

        #remember stock status
        url["prev_instock"] = url["curr_instock"]

    #send email if something is found in stock
    if email_body != "":
        email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, email_body)

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

    email_body = ""

    # wait for 5min for the next check
    print('+++++ 5 min +++++')
    time.sleep(300)

driver.quit()
