from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.supremenewyork.com/shop/jackets/qfpku5g0o/ulxwta3b9')
elem1 = driver.find_element_by_link_text('add-remove-buttons')
elem1.click()



#add-remove-buttons