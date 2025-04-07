import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1345x610")
driver = webdriver.Chrome(options=options)
driver.set_window_size(1354, 610)
actions = ActionChains(driver)
print("script started")

driver.get("https://bdgame.in/code/die.html")
time.sleep(5)

textarea_element = driver.find_element("id", "lion")

code = textarea_element.get_attribute('value')

with open("die.py", "w") as file:
    file.write(code)
driver.quit()
result = subprocess.run(["python3", "die.py"], capture_output=True, text=True)
print("Output of die.py:", result.stdout)
