from selenium import webdriver
import time

driver = webdriver.Chrome()


usr = input('Enter Email Id: ')
pwd = input('Enter Password: ')

driver.get('https://www.facebook.com/')
print ("Opening Facebbok")
time.sleep(1)
print('Opened Facebook')

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print("Email Id entered")

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("Passwored entered")

login_box = driver.find_element_by_id('loginbutton')
login_box.click()


print("Done")
input('Press enter to quit')
quit()

print("Finished")
