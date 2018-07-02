import sys
import io
from selenium import webdriver
import time
# from selenium.webdriver.chrome.options import Options


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# chrome_options.add_argument('--log-level=3')
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('C:/section3/webdriver/chrome/chromedriver')

driver.set_window_size(1920, 1280)
driver.implicitly_wait(3)

driver.get('https://wishket.com/accounts/login/')
time.sleep(7)
driver.implicitly_wait(3)
driver.find_element_by_name('identification').send_keys('dashiki')
driver.implicitly_wait(1)
driver.find_element_by_name('password').send_keys('c20026495538')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/div/button').click()

driver.quit()
