import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='D:\Documents\chromedriver.exe',options=chrome_options)
lat = 18.9817693
lng = 79.9570682
z = 14
url = 'https://www.google.com/maps/@' + str(lat) + ',' + str(lng) +',' + str(z) + 'z'
driver.get(url)
achains = ActionChains(driver)
time.sleep(2)
right_click = driver.find_element_by_xpath("//body")
achains.context_click(right_click).perform()
time.sleep(2)
what = driver.find_element_by_css_selector(".nbpPqf-menu-x3Eknd[aria-checked='false'][data-index='3']")
what.click()
time.sleep(1)
pincode = driver.find_element_by_xpath("//div[@class='GaSlwc-uhFGfc-WsjYwc-Q7Zjwb-RWgCYc']").text
print(pincode)
