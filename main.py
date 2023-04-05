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


if __name__ == '__main__':
    driver = webdriver.Edge(executable_path="msedgedriver")
    url = ('https://www.gateway2jordan.gov.jo/transitJO/')
    #while(datetime.datetime.now().minute < 15 ):
    for i in range(4):
        driver.get(url)
        driver.find_element(By.NAME, "txtName").send_keys('jhbksj')
        driver.find_element(By.XPATH, '/html/body/form/section/div/div/div[3]/div[1]/div[4]/div[2]/div[1]/label' ).click()
        driver.find_element(By.XPATH, '/html/body/form/section/div/div/div[3]/div[1]/div[5]/div[2]/select/option[8]' ).click()
        driver.find_element(By.XPATH, '/html/body/form/section/div/div/div[3]/div[1]/div[19]/div/label' ).click()
        driver.find_element(By.NAME,'FileUpload1').send_keys(r'C:\Users\Muhammad\Desktop\pythonProject\muh.jpg')
        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[i+1])

    time.sleep(5)
    driver.quit()



