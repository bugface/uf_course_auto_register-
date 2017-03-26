'''
######################################################
@author: Xi Yang                                     #
@os environment: linux                               #
@pre-required package: sox, chrome-driver            #
@running environment: python3.X                      #
@pre-required package: selenium                      #
@pre-config: put the chrome-drive under  /usr/bin/   #
@result: when course been found, there will be a beep#
	sound for 3s                                     #
@make relevent changes based on comments in the code #
@adjust time in each sleep() based on your web speed #
@program might collapse after a period of time due   #
	to chrome_driver                                 #
@you might need to modify for page or other changes	 #
######################################################
'''

from selenium import webdriver
import os
from time import sleep

#define which driver we will use
chrome_driver = "/usr/bin/chromedriver"
#add the chrome_driver into the os environment
os.environ["webdriver.chrome.driver"]  = chrome_driver

# def main():
	#chage the course to what you want to search
course = "XXXX"

flag = 1

while(flag):
	try:
		browser = webdriver.Chrome(chrome_driver)
		#if does not work, use http instead of https
		browser.get("https://www.student.ufl.edu")
		sleep(5)

		logout = browser.find_element_by_class_name("logout-btn")
		logout.click()
		sleep(2)

		spring = browser.find_element_by_link_text("Spring")
		spring.click()
		sleep(5)

		box1 = browser.find_element_by_id("username")
		#add your username
		box1.send_keys("xxxxxxx")
		box2 = browser.find_element_by_id("password")
		#add your password
		box2.send_keys("*********")

		submit = browser.find_element_by_id("submit")
		submit.click()
		sleep(3)

		all1 = browser.find_element_by_link_text("Search All Courses")
		all1.click()
		sleep(1)

		#if you need courses from other department, replace 'COMPUTER & INFO SCI & ' with your department abbv
		cs = browser.find_element_by_xpath("//option[@value='COMPUTER & INFO SCI & ']")
		cs.click()
		search = browser.find_element_by_xpath("//input[@value='Search']")
		search.click()
		sleep(3)

		tds = browser.find_elements_by_tag_name("td")
		flag1 = 0
		for td in tds:
			if td.text == course:
				os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (3, 450))
				flag = 0
				flag1 = 1
				break;

		while(not flag1):
			sections = browser.find_element_by_xpath("//input[@value='Show More sections']")
			if sections == None:
				flag1 = 1
			sections.click()
			tds = browser.find_elements_by_tag_name("td")
			for td in tds:
				if td.text == course:
					os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (3, 450))
					flag = 0
					break
		if flag:
			browser.quit()
	except:
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1, 650))
		browser.quit()
#main()

# if __name__ == "__main__":
#     main()


