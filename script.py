template = '''import time
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

driver.get("https://bdgame.in/code/Pytho_code_{index}.html")
time.sleep(5)

textarea_element = driver.find_element("id", "lion")

code = textarea_element.get_attribute('value')

with open("pythoncode{index}.py", "w") as file:
    file.write(code)
driver.quit()
result = subprocess.run(["python3", "pythoncode{index}.py"], capture_output=True, text=True)
print("Output of pythoncode{index}.py:", result.stdout)'''

with open("gen_script.py", "w") as f:
    for i in range(1, 13):
        variable = f"pyco{i} = '''{template.format(index=i)}'''\n\n"
        f.write(variable)

print("✅ File 'gen_script.py' created with pyco1 to pyco12.")
