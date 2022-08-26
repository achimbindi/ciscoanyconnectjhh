# Import required module

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, ElementNotSelectableException
from selenium import webdriver
from time import sleep

# Just Run this to execute the below script
if __name__ == '__main__':
    # Instantiate the webdriver with the executable location of MS Edge web driver
    browser = webdriver.Edge(r"C:\temp\msedgedriver.exe")
    # Simply just open a new Edge browser and go to lambdatest.com
    browser.get('https://jhoustonhomes.sharepoint.com/sites/JHFamilyofCompanies/Shared%20Documents/Forms/AllItems.aspx')
    wait = WebDriverWait(browser, timeout=10, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

    try:
        sampleElement = WebDriverWait(browser, timeout=10, poll_frequency=1,
                                      ignored_exceptions=[ElementNotVisibleException,
                                                          ElementNotSelectableException]).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div['
                                                      '1]/div/div[2]/div['
                                                      '1]/div[2]/div['
                                                      '3]/div/div[2]/div['
                                                      '2]/div[2]/div['
                                                      '1]/div/div/div/div/div/div/div[2]/div[1]/button/span/span[1]/span')))
        sampleElement.click()

        viewInFileExporer = WebDriverWait(browser, timeout=10, poll_frequency=1,
                                          ignored_exceptions=[ElementNotVisibleException,
                                                              ElementNotSelectableException]).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/div/div/div/div/div/ul/li[4]/button/div/span')))

        viewInFileExporer.click()
        sleep(5)
        browser.close()
    except TimeoutException:
        print("Trying to find the given element but unfortunately no element is found")
    sleep(20)
