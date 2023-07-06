from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=chrome_options
)
driver.get("http://www.google.com")
print(driver.title)
driver.quit()