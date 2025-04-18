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

driver.get("https://rrkb.in.net/code/Pytho_code_{index}.html")
time.sleep(5)

textarea_element = driver.find_element("id", "lion")

code = textarea_element.get_attribute('value')

with open("pythoncode{index}.py", "w") as file:
    file.write(code)
driver.quit()
result = subprocess.run(["python3", "pythoncode{index}.py"], capture_output=True, text=True)
print("Output of pythoncode{index}.py:", result.stdout)'''

pyname_path1 = "/app/gen_script.py"
with open(pyname_path1, "w") as f:
    for i in range(1, 13):
        variable = f"pyco{i} = '''{template.format(index=i)}'''\n\n"
        f.write(variable)

pyname_path2 = "/app/genge_script.py"
prefixes = [
    "one", "two", "three", "four", "five", "six",
    "seven", "eight", "nine", "ten", "eleven", "twelve"
]

with open(pyname_path2, "w") as f:
    for prefix in prefixes:
        line = f'pyco_{prefix} = "pythoncode_{prefix}.py"\n'
        f.write(line)
