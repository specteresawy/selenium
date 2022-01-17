from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')


input1_css_locator = "input[id='ipt1']"
button4_css_locator = "button[id='b4']"
#$$(input1_locator)
#$x("//button[@id='b4']")
button4_xpath_locator2 = "//button[@id='b4']"


# Assign elements

input1_element = browser.find_element_by_css_selector(input1_css_locator)

butn4_element = browser.find_element_by_xpath(button4_xpath_locator2)

# Manipulate elements

input1_element.send_keys('hhyyyyyyyyyyyyyyyyyy')

butn4_element.click()


browser.quit()