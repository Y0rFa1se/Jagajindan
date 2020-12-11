from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("elements/cd/cd_87.0.4280.88.exe")
driver.get("https://hcs.eduro.go.kr/#/loginWithUserInfo")

def login():
    go = driver.find_element_by_id("btnConfirm2")
    go.click()

    #find schoolName
    scName = driver.find_element_by_class_name("searchBtn")
    scName.click()

    scName = Select(driver.find_element_by_id("sidolabel"))
    scName.select_by_value("01")

    scName = Select(driver.find_element_by_id("crseScCode"))
    scName.select_by_value("4")

    scName = driver.find_element_by_id("orgname")
    scName.send_keys("자운고등학교")

    scName = driver.find_element_by_class_name("searchBtn")
    scName.click()

    scName = driver.find_element_by_class_name("layerSchoolArea")
    scName.click()

    scName = driver.find_element_by_xpath("//*[text() = '자운고등학교']")
    scName.click()

    scName = driver.find_element_by_class_name("layerFullBtn")
    scName.click()

    #name/DoB
    id = driver.find_element_by_id("user_name_input")
    id.send_keys("이은준")

    id = driver.find_element_by_id("birthday_input")
    id.send_keys("030317")

    go = driver.find_element_by_id("btnConfirm")
    go.click()

    #pw
    time.sleep(0.1)
    pw = driver.find_element_by_class_name("input_text_common")
    pw.send_keys("6974")

    go = driver.find_element_by_id("btnConfirm")
    go.click()

login()

with open("elements/list.ini", "r", encoding="utf-8") as men_lists:
    lists = men_lists.readlines()
    for name in lists:
        time.sleep(1)
        index = driver.find_element_by_xpath("//span[text()=' " + name.replace("\n", "") + " ']")
        index.click()
        time.sleep(1)
        surv = driver.find_element_by_id("survey_q1a1")
        surv.click()
        surv = driver.find_element_by_id("survey_q2a1")
        surv.click()
        surv = driver.find_element_by_id("survey_q3a1")
        surv.click()
        surv = driver.find_element_by_id("btnConfirm")
        surv.click()
        home = driver.find_element_by_xpath("//span[text()='처음으로']")
        home.click()
        time.sleep(1)