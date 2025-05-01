from selenium.webdriver.common.by import By
import os
from selenium.common.exceptions import NoSuchElementException
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from all_git_passes import userid, passid , gitid, gitpass, gitdashboard, gitnew, gitprofie, gitreponame, giturl, gitlogurl, gitblankfile, docke1, dokereponame, workflowname, crreateanewblankworkflow, newfie, newfiereponame, pyco1, pyco2, pyco3, pyco4, pyco5, pyco6, pyco7, pyco8, pyco9, pyco10, pyco11, pyco12, pyco_one, pyco_two, pyco_three, pyco_four, pyco_five, pyco_six, pyco_seven, pyco_eight, pyco_nine, pyco_ten, pyco_eleven, pyco_twelve
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

Windows_10_Chrome = "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
Ubuntu_Linux_Chrome = "--user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
macOS_Chrome = "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
Android_Chrome = "--user-agent=Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
Windows_10_Firefox = "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/137.0"
Ubuntu_Linux_Firefox = "--user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/137.0"
macOS_Firefox = "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:123.0) Gecko/20100101 Firefox/137.0"
Android_Firefox = "--user-agent=Mozilla/5.0 (Android 13; Mobile; rv:123.0) Gecko/123.0 Firefox/137.0"
Windows_10_Edge = "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/123.0.0.0"
macOS_Edge = "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/123.0.0.0"
macOS_Safari = "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/18.0 Safari/537.36"
iPhone_Safari = "--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/537.36"
iPad_Safari = "--user-agent=Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/537.36"
Internet_Explorer_11_Windows_10 = "--user-agent=Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko"

Fool = ['Windows_10_Chrome', 'Android_Chrome', 'Ubuntu_Linux_Chrome', 'iPhone_Safari', 'Android_Chrome', 'Windows_10_Chrome', 'macOS_Chrome', 'Android_Chrome', 'Windows_10_Chrome', 'Android_Chrome', 'iPhone_Safari', 'Android_Chrome', 'Windows_10_Firefox', 'Android_Chrome', 'iPhone_Safari', 'Android_Chrome', 'Ubuntu_Linux_Firefox', 'Android_Chrome', 'iPhone_Safari', 'Android_Chrome', 'macOS_Firefox', 'Android_Chrome', 'iPhone_Safari', 'Android_Firefox', 'macOS_Safari', 'Android_Chrome', 'iPhone_Safari', 'Android_Chrome', 'Internet_Explorer_11_Windows_10', 'Android_Chrome', 'Windows_10_Edge', 'Windows_10_Chrome', 'Android_Chrome']
Fool_bro = random.choice(Fool)

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(f"--user-agent={Fool_bro}")
options.add_argument("--window-size=1345x610")
driver = webdriver.Chrome(options=options)
driver.set_window_size(1354, 610)
actions = ActionChains(driver)
print("script started")
driver.get("https://account.proton.me/mail")
time.sleep(random.uniform(10,30))

def boiled (Keys,ActionChains,driver):
    ActionChains(driver).send_keys("name: Docker Image CI").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("on:").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  push:").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys('''  branches: [ "main" ]''').perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("pull_request:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys('''  branches: [ "main" ]''').perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("jobs:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  build:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys("    runs-on: ubuntu-latest").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("outputs:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("  matrix: ${{ steps.set-matrix.outputs.matrix }}").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys("steps:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  - name: Checkout code").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  uses: actions/checkout@v4").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("- name: Build the Docker image").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  run: docker build -t my-app .").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys("- name: Save Docker image to file").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  run: docker save my-app > my-app.tar").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("- name: Upload image artifact").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  uses: actions/upload-artifact@v4").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("with:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  name: my-app-image").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("path: my-app.tar").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys("- name: Set matrix output").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  id: set-matrix").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("run: |").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys('''  echo "matrix=$(jq -c '{scripts: ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]}' <<< '{}')" >> "$GITHUB_OUTPUT"''').perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("run-pythoncode:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  needs: build").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("runs-on: ubuntu-latest").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("strategy:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  max-parallel: 1  # Ensures sequential execution").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("matrix: ${{fromJson(needs.build.outputs.matrix)}}").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys("steps:").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  - name: Download Docker image artifact").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("  uses: actions/download-artifact@v4").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("with:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("  name: my-app-image").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys("- name: Load Docker image").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  run: docker load < my-app.tar").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys('''- name: Run pythoncode_${{ matrix.scripts }}.py''').perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys('''  run: docker run --rm my-app python3 pythoncode_${{ matrix.scripts }}.py''').perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys("run_rebirth:").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  needs: run-pythoncode").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("runs-on: ubuntu-latest").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("steps:").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  - name: Download Docker image artifact").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  uses: actions/download-artifact@v4").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("with:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("  name: my-app-image").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys("- name: Load Docker image").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  run: docker load < my-app.tar").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("- name: Run python_rebirth.py").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("  run: docker run --rm my-app python3 python_rebirth.py").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys("run_die:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("  needs: run_rebirth").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("runs-on: ubuntu-latest").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("steps:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("  - name: Download Docker image artifact").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  uses: actions/download-artifact@v4").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("with:").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys("  name: my-app-image").perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys("- name: Load Docker image").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("  run: docker load < my-app.tar").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("- name: Run python_die.py").perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.uniform(1,8))
    ActionChains(driver).send_keys("  run: docker run --rm my-app python3 python_die.py").perform()


def kinih (userid,passid):
    global veric
    driver.execute_script("window.open('');") #to open another tab
    driver.switch_to.window(driver.window_handles[1]) #to switch to 2nd tab
    time.sleep(random.uniform(10,25))


    try:
        driver.get("https://account.proton.me/mail")
    except Exception as e:
        print("Element not found:", str(e))   
    
    time.sleep(random.uniform(2,10))
    driver.find_element("id", "username").send_keys(userid)

    try:
        pasta_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
    except Exception as e:
        print("Element not found:", str(e))
        time.sleep(random.uniform(5,10))
    pasta_name.send_keys(passid)

    button_xpath = '/html/body/div[1]/div[4]/div[1]/main/div[1]/div[2]/form/button'

    button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )
    button_element.click()
    time.sleep(random.uniform(40,100))
    driver.execute_script("window.open('');") #to open another tab
    driver.switch_to.window(driver.window_handles[2]) #to switch to 3nd tab
    time.sleep(random.uniform(5,10))
    driver.get("https://account.proton.me/mail")
    time.sleep(random.uniform(20,60))
    cenx = 400
    ceny = 100
    time.sleep(30)
    actions.move_by_offset(0, 0).click().perform()
    actions.move_by_offset(cenx, ceny).click().perform()
    actions.move_by_offset(cenx, ceny).click().perform()
    time.sleep(random.uniform(40,100))

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

    # Locate the element inside the iframe
    ema = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "proton-root"))
    )
    emx = ema.text

    print(emx)
    print("loream break\n")

    # exit iframe code 
    driver.switch_to.default_content()
    match = re.findall(r'\b\d{6}\b', emx)

    if match:
        verio = (f"{match[0]}")
    else:
        print("no code found")
    time.sleep(random.uniform(5,10))
    veric = (f"{match[0]}")
    manc = int(veric)
    driver.close()

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(random.uniform(10,20))

    driver.find_element("id", "otp").send_keys(manc)
    time.sleep(random.uniform(5,20))



try:
    driver.get(gitlogurl)
except Exception as e:
    print("Element not found:", str(e))   
time.sleep(random.uniform(20,50))

driver.find_element("id", "login_field").send_keys(gitid)
time.sleep(random.uniform(15,40))
driver.find_element("id", "password").send_keys(gitpass)
time.sleep(random.uniform(15,40))

log_btu = '//*[@id="login"]/div[4]/form/div/input[13]'

bllllo_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, log_btu))
    )
bllllo_element.click()
time.sleep(random.uniform(15,50))
try:
    king_kilo = driver.find_element("id", "otp")
    time.sleep(random.uniform(5,10))
    kinih (userid,passid)
except NoSuchElementException:
    print("DEVICE VERIFICATION NOT NEEDED")
    
driver.get(gitnew)
time.sleep(random.uniform(15,60))
try:
    fillo = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=":r5:"]')))
    time.sleep(random.uniform(5,10))
    fillo.send_keys(gitreponame)
except NoSuchElementException:
    print("error")
time.sleep(random.uniform(5,10))
crtbutton = driver.find_element(By.XPATH, "//button[span/span[text()='Create repository']]")
crtbutton.click()
time.sleep(random.uniform(8,20))


def carkichabi (contentoo, naamoo):
    driver.get(gitblankfile)
    time.sleep(random.uniform(8,20))
    ActionChains(driver).send_keys(contentoo).perform()
    time.sleep(random.uniform(20,50))

    djrockk = '//*[@id="repo-content-pjax-container"]/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/span[2]/input'
    sanataan = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, djrockk))
        )
    sanataan.send_keys(naamoo)

    crtbutton = driver.find_element(By.XPATH, "//button[span/span[text()='Commit changes...']]")
    crtbutton.click()
    time.sleep(random.uniform(5,15))
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    time.sleep(random.uniform(5,50))



carkichabi (pyco_eight, pyco8)
carkichabi (pyco_four, pyco4)
carkichabi (pyco_twelve, pyco12)
carkichabi (pyco_nine, pyco9)
carkichabi (pyco_six, pyco6)
carkichabi (pyco_three, pyco3)
carkichabi (pyco_eleven, pyco11)
carkichabi (pyco_two, pyco2)
carkichabi (pyco_seven, pyco7)
carkichabi (pyco_one, pyco1)
carkichabi (pyco_ten, pyco10)
carkichabi (pyco_five, pyco5)


driver.get(gitblankfile)
time.sleep(random.uniform(8,20))
ActionChains(driver).send_keys(docke1).perform()
time.sleep(random.uniform(20,50))

djrockk = '//*[@id="repo-content-pjax-container"]/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/span[2]/input'
sanataan = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, djrockk))
    )
sanataan.send_keys(dokereponame)

crtbutton = driver.find_element(By.XPATH, "//button[span/span[text()='Commit changes...']]")
crtbutton.click()
time.sleep(random.uniform(5,15))
ActionChains(driver).send_keys(Keys.ENTER).perform()

time.sleep(random.uniform(5,50))


driver.get(crreateanewblankworkflow)
time.sleep(random.uniform(50,200))

# Start boilerplate
boiled(Keys, ActionChains, driver)


time.sleep(random.uniform(10,50))
crtbutton = driver.find_element(By.XPATH, "//button[span/span[text()='Commit changes...']]")
crtbutton.click()
time.sleep(random.uniform(5,15))
ActionChains(driver).send_keys(Keys.ENTER).perform()


time.sleep(random.uniform(50,100))
driver.quit()
