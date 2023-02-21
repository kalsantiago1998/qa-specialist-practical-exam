from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium_demo():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver.maximize_window()

    driver = webdriver.Chrome(options=options)
    driver.get("https://titan22.com/account/register")

    firstName = driver.find_element(By.ID, "FirstName")
    firstName.clear()
    firstName.send_keys("Juan")

    lastName = driver.find_element(By.ID, "LastName")
    lastName.clear()
    lastName.send_keys("Dela Cruz")

    email = driver.find_element(By.ID, "Email")
    email.clear()
    email.send_keys("juandelacruz@yopmail.com")

    password = driver.find_element(By.ID, "CreatePassword")
    password.clear()
    password.send_keys("password@1234")

    password = driver.find_element(By.ID, "CreatePassword")
    password.clear()
    password.send_keys("password@1234")

    custAcceptTerms = driver.find_element(By.ID, "customer[accepts_terms]")
    custAcceptTerms.click()

    submit = driver.find_element(By.CLASS_NAME,"button button--primary")
    submit.click()
 

