from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
import pandas as pd


def execute():
    file = pd.read_csv(r'final.csv', header=0)
    driver = webdriver.Edge(executable_path="msedgedriver.exe")
    url = ('https://visitjordan.gov.jo/travelcars/')
    for i in range(len(file.index)):
        driver.get(url)
        driver.find_element(By.XPATH,'/html/body/form/section/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/input').click()
        driver.find_element(By.NAME, "txtName").send_keys(file['الاسم'][i])
        driver.find_element(By.XPATH,'/html/body/form/section/div/div/div[3]/div[1]/div[5]/div[2]/select/option[3]').click()
        driver.find_element(By.NAME, "txtPassportNu").send_keys(file['رقم جواز السفر'][i])
        driver.find_element(By.NAME, "txtIDNumber").send_keys(file['الرقم الوطني'][i])
        driver.find_element(By.NAME, "txtCarNumber").send_keys(file['رقم السيارة'][i])
        driver.find_element(By.NAME, "txtEmail").send_keys(file['البريد الالكتروني'][i])
        driver.find_element(By.XPATH,'/html/body/form/section/div/div/div[3]/div[1]/div[10]/div[2]/select/option[3]').click()
        driver.find_element(By.NAME, "txtMobile").send_keys(file['رقم الاتصال'][i])
        driver.find_element(By.XPATH,'/html/body/form/section/div/div/div[3]/div[1]/div[12]/div[2]/div/div/input[2]"]').send_keys(file['جواز السفر'][i] + 'jpg')
        driver.find_element(By.XPATH, '/html/body/form/section/div/div/div[3]/div[1]/div[13]/div/input').click()
        driver.find_element(By.XPATH, '/html/body/form/section/div/div/div[3]/div[3]/div/input[3]').click()

def start():
    while True:
        now = datetime.datetime.now()
        if now.hour == 21 and 0 <= now.minute < 5:
            execute()
        time.sleep(2)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.binary_location = os.environb.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument('--window-size=1920,1080')
    #myDriver = webdriver.Chrome(executable_path=os.environb.get("CHROMEDRIVER_PATH") , chrome_options= chrome_options)
    prefs = {"profile.managed_default_content_settings.images": 2}
    #chrome_options.headless = True

    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver


if __name__ == '__main__':
    driver = createDriver()
    url = ('https://www.gateway2jordan.gov.jo/transitJO/')
    driver.get(url)
    driver.find_element(By.NAME, "txtName").send_keys('jhbksj')

    driver.find_element(By.XPATH, '/html/body/form/section/div/div/div[3]/div[1]/div[4]/div[2]/div[1]/label' ).click()
    driver.find_element(By.XPATH, '/html/body/form/section/div/div/div[3]/div[1]/div[5]/div[2]/select/option[8]' ).click()
    driver.find_element(By.XPATH, '/html/body/form/section/div/div/div[3]/div[1]/div[19]/div/label' ).click()
    driver.find_element(By.NAME,'FileUpload1').send_keys(r'C:\Users\Muhammad\Desktop\pythonProject\muh.jpg')

    time.sleep(20)
    driver.quit()




