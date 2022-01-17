from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/trial-of-the-stones')

#riddle of the stones

input_element = browser.find_element_by_css_selector('input[id="r1Input"]')

input_element.send_keys('rock')

button = browser.find_element_by_css_selector('button[id="r1Btn"]')

button.click()


#riddle of the secrets


#the two merchants

