from selenium import webdriver

#driver=webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe")

from webdriver_manager.chrome import ChromeDriverManager    
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://titan22.com/account/register")

driver.find_element_by_id("FirstName").send_keys("Juan")
driver.find_element_by_id("LastName").send_keys("Dela Cruz")
driver.find_element_by_id("Email").send_keys("juandelacruz@yopmail.com")
driver.find_element_by_id("CreatePassword").send_keys("password@1234")
driver.find_element_by_id("customer[accepts_terms]").click()
driver.find_element_by_type("submit").click()

print('Driver Title',driver.title)
print('Driver Name',driver.name)
print('Driver URL',driver.current_url)

