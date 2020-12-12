from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("elements/cd/cd_87.0.4280.88.exe")
driver.get("https://hcs.eduro.go.kr/#/loginWithUserInfo")

with open("elements/mainElements.ini", "r", encoding="utf-8") as mElements:
    cp_name = mElements.readline().replace("\n", "")
    sc_level = mElements.readline().replace("\n", "")
    sc_name = mElements.readline().replace("\n", "")
    u_name = mElements.readline().replace("\n", "")
    u_dob = mElements.readline().replace("\n", "")
    u_pw = mElements.readline().replace("\n", "")
    print(cp_name, sc_level, sc_name, u_name, u_dob, u_pw)


def login():
    go = driver.find_element_by_id("btnConfirm2")
    go.click()
    time.sleep(1)

    #schoolName
    scName = driver.find_element_by_class_name("searchBtn")
    scName.click()
    time.sleep(1)

    scName = Select(driver.find_element_by_id("sidolabel"))
    scName.select_by_visible_text(cp_name)

    scName = Select(driver.find_element_by_id("crseScCode"))
    scName.select_by_visible_text(sc_level)

    scName = driver.find_element_by_id("orgname")
    scName.send_keys(sc_name)

    scName = driver.find_element_by_class_name("searchBtn")
    scName.click()

    scName = driver.find_element_by_class_name("layerSchoolArea")
    scName.click()

    scName = driver.find_element_by_xpath("//*[text() = '" + sc_name + "']")
    scName.click()

    scName = driver.find_element_by_class_name("layerFullBtn")
    scName.click()
    time.sleep(1)

    #name/DoB
    id = driver.find_element_by_id("user_name_input")
    id.send_keys(u_name)

    id = driver.find_element_by_id("birthday_input")
    id.send_keys(u_dob)

    go = driver.find_element_by_id("btnConfirm")
    go.click()

    #pw
    time.sleep(1)
    pw = driver.find_element_by_class_name("input_text_common")
    pw.send_keys(u_pw)

    go = driver.find_element_by_id("btnConfirm")
    go.click()
def survey(order):
    time.sleep(1)
    index = driver.find_element_by_xpath("//span[text()=' " + order + " ']")
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

login()

with open("elements/list.ini", "r", encoding="utf-8") as men_lists:
    lists = men_lists.readlines()
    for name in lists:
        nameOrder = name.replace("\n", "")
        try:
            survey(nameOrder)
            print("surveyed " + nameOrder)

        except:
            print("passed " + nameOrder)
            pass