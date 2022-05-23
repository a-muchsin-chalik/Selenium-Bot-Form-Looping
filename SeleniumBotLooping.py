# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# open Chrome
driver = webdriver.Chrome(
	'C:/Users/Acer/Music/chromedriver.exe')

# Open URL
driver.get('https://printing.sublimaxdigital.com/hubungi-kami/')

# wait for one second, until page gets fully loaded
time.sleep(1)

# Data
datas = [
	['Mary D Joiner', 'MaryDJoiner@gmail.com', '4079025063', '2474 McDonald Avenue,Maitland'],
	['Karen B Johnson', 'KarenBJohnson@gmail.com', '3153437575', '2143 Oak Street,GRAND ISLE'],
]

# Iterate through each data
for data in datas:
	# Initialize count is zero
	count = 0

	# contain input boxes
	textboxes = driver.find_elements_by_class_name(
		"forminator-input")

	# contain textareas
	textareaboxes = driver.find_elements_by_class_name(
		"forminator-textarea")

	# Iterate through all input boxes
	for value in textboxes:
		# enter value
		value.send_keys(data[count])
		# increment count value
		count += 1

	# Iterate through all textareas
	for value in textareaboxes:
		# enter value
		value.send_keys(data[count])
		# increment count value
		count += 1

	# click on submit button
	submit = driver.find_element_by_xpath(
        '//*[@id="forminator-module-1247"]/div[8]/div/div/button')
	submit.click()

	# fill another response
	time.sleep(10)

# close the window
driver.close()
