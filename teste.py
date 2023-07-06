from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=chrome_options
)

driver.get("https://www.vagalume.com.br/top100/musicas/")
musicas = driver.find_elements(By.CSS_SELECTOR, "a.w1")
for musica in musicas:
    print(musica.text)
    sleep(1)

driver.quit()