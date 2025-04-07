from selenium.webdriver.common.by import By
import os
from selenium.common.exceptions import NoSuchElementException
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from all_git_passes import userid, passid , gitid, gitpass, gitdashboard, gitnew, gitprofie, gitreponame, giturl, gitlogurl, gitblankfile, docke1, dokereponame, workflowname, crreateanewblankworkflow, newfie, newfiereponame, workingflow, seting
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"  # Path to the Chromium binary
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")  # Disable sandboxing
options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
options.add_argument("--window-size=1345x610")
driver = webdriver.Chrome(options=options)
driver.set_window_size(1354, 610)
actions = ActionChains(driver)
print("script started")
driver.get("https://account.proton.me/mail")
time.sleep(10)

def kinih (userid,passid):
    global veric
    driver.execute_script("window.open('');") #to open another tab
    driver.switch_to.window(driver.window_handles[1]) #to switch to 2nd tab
    time.sleep(10)


    try:
        # Open the webpage
        driver.get("https://account.proton.me/mail")
    except Exception as e:
        print("Element not found:", str(e))   
    
    driver.find_element("id", "username").send_keys(userid)

    try:
        pasta_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
    except Exception as e:
        print("Element not found:", str(e))
        time.sleep(5)
    pasta_name.send_keys(passid)

    button_xpath = '/html/body/div[1]/div[4]/div[1]/main/div[1]/div[2]/form/button'

    button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )
    button_element.click()
    time.sleep(60)
    driver.execute_script("window.open('');") #to open another tab
    driver.switch_to.window(driver.window_handles[2]) #to switch to 3nd tab
    time.sleep(10)
    driver.get("https://account.proton.me/mail")
    time.sleep(30)
    cenx = 400
    ceny = 100
    time.sleep(30)
    actions.move_by_offset(0, 0).click().perform()
    actions.move_by_offset(cenx, ceny).click().perform()
    actions.move_by_offset(cenx, ceny).click().perform()
    print("clicker")
    time.sleep(50)

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

    # Locate the element inside the iframe
    ema = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "proton-root"))
    )
    emx = ema.text

    # Print the email content
    print(emx)
    print("loream break\n")

    # exit iframe code 
    driver.switch_to.default_content()
    match = re.findall(r'\b\d{6}\b', emx)

    if match:
        verio = (f"{match[0]}")
        print("code is:: ", verio)
    else:
        print("no code found")
    time.sleep(10)
    veric = (f"{match[0]}")
    manc = int(veric)
    print(manc)
    driver.close()

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(10)

    driver.find_element("id", "otp").send_keys(manc)
    time.sleep(20)



try:
    # Open the webpage
    driver.get(gitlogurl)
except Exception as e:
    print("Element not found:", str(e))   
time.sleep(30)

driver.find_element("id", "login_field").send_keys(gitid)
time.sleep(25)
driver.find_element("id", "password").send_keys(gitpass)
time.sleep(15)

log_btu = '//*[@id="login"]/div[4]/form/div/input[13]'

bllllo_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, log_btu))
    )
bllllo_element.click()
time.sleep(20)
try:
    king_kilo = driver.find_element("id", "otp")
    time.sleep(5)
    kinih (userid,passid)
except NoSuchElementException:
    print("DEVICE VERIFICATION NOT NEEDED")
    
#further automations
driver.get(seting)
time.sleep(10)
delbutton = driver.find_element(By.XPATH, '//*[@id="dialog-show-repo-delete-menu-dialog"]')
delbutton.click()
time.sleep(10)
delfi = driver.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]')
delfi.click()
time.sleep(10)
delfi2 = driver.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]')
delfi2.click()
time.sleep(10)

inpbo = driver.find_element(By.ID, "verification_field")
repo_value = inpbo.get_attribute("data-repo-nwo")

inpbo.send_keys(repo_value)
time.sleep(10)
delfi2 = driver.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]')
delfi2.click()

driver.quit()
