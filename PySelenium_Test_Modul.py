from selenium import webdriver
from selenium.common.exceptions import *
import time
import logging
import os


class test_class:
	def __init__(self, link, driver):
		new_dir = r'./log_directory'
		print('logs are located in directory: "log_directory"')
		if not os.path.exists(new_dir):
			    os.makedirs(new_dir)
		logging.basicConfig(level=logging.INFO, filename="./log_directory/automatic_test_log.log")

		global log
		log = logging.getLogger('loger')
		global log_time
		log_time = (time.ctime())		
		log.info('\n _______________________________________________________\n')
		log.info('Start Test {}'. format(log_time))


		self.driver = driver
		log.info('Browser: ' + self.driver.name)
		self.driver.get(link)
		

		
	'''
	//////////////////////////////////////////////////////////////////////////////////////
	Initialize the browser, start logging, create a directory for storing logs.
	//////////////////////////////////////////////////////////////////////////////////////
	'''



	def search_class(self, name_element):
		try: 	
			self.search_form = self.driver.find_element_by_class_name(name_element)
			log.info('Element ' +  name_element + ' found')
			log.info('Element displayed: {}'. format(self.search_form.is_displayed()))
			return self.search_form
		except NoSuchElementException:
			log.exception('Element ' + name_element + ' not found');

	'''
	/////////////////////////////////////////////////////////////////////////////////////////
	The function of finding an element by the class_name, including checking its
	display on the page with entering the result into the logs.
	//////////////////////////////////////////////////////////////////////////////////////////
	'''




	def search_xpath(self, name_element):
		try: 
			self.search_form = self.driver.find_element_by_xpath(name_element)
			log.info('Element ' + name_element + ' found')
			log.info('Element displayed: {}'. format(self.search_form.is_displayed()))
			return self.search_form

		except NoSuchElementException:		
			log.exception('Element ' + name_element + ' not found');
		
			

	'''
	//////////////////////////////////////////////////////////////////////////////////////////
	The function of finding an element by xpath, including checking its display on the page,
	with entering the result into the logs.
	//////////////////////////////////////////////////////////////////////////////////////////		
	'''


	def search_css(self, name_element):
		try:
			self.search_form = self.driver.find_element_by_css_selector(name_element)
			log.info('Element ' + name_element + ' found')
			log.info('Element displayed: {}'. format(self.search_form.is_displayed()))
			return self.search_form

		except NoSuchElementException:			
			log.exception('Element ' + name_element + ' not found');

		
	'''
	//////////////////////////////////////////////////////////////////////////////////////////
	The function of searching for an element by css_selector, including checking its display
	on the page, with entering the result into the logs.
	//////////////////////////////////////////////////////////////////////////////////////////		
	'''

	def image(self, name_tag):
		try:
			link = self.driver.find_element_by_tag_name(name_tag)	
			src = link.get_attribute("src")
			log.info('Element ' +  name_tag + ' found')
			log.info('Element displayed: {}'. format(self.search_form.is_displayed()))
			log.info(src)

		except NoSuchElementException:			
			log.exception('Element ' + name_tag+ ' not found');
	'''
	/////////////////////////////////////////////////////////////////////////////////////////////	
	The function of searching for images by tag_name, including checking the display of the
	desired image on the page, with entering the result in the logs.
	/////////////////////////////////////////////////////////////////////////////////////////////		
	'''


	def image_check(self, test_image, name_tag):
		try:
			link = self.driver.find_element_by_tag_name(name_tag)	
			src = link.get_attribute("src")
			image_data=src
			if test_image:
				link = self.driver.find_element_by_tag_name(name_tag)	
				src = link.get_attribute("src")
				image_data_1 = src
				log.info('{} \n {} \n'. format(image_data, image_data_1)) 
				if image_data == image_data_1:
					log.info('This is the first Image')
				else: 
					log.info('This is not first Image')

		except NoSuchElementException:			
			log.exception('Element ' + name_tag+ ' not found');



	'''
	////////////////////////////////////////////////////////////////////////////////////////////////
	The function of searching for an image by the tag_name, comparing it with the original image to
	be searched, including checking its display on the page, with entering the result in the logs.
	////////////////////////////////////////////////////////////////////////////////////////////////
	'''

	def text_to_searchTab(self, name_element, text, suggest_tabs):
		

		try:
			self.search_xpath(name_element).send_keys(text)			 	 
			self.search_form.click()						
		except NoSuchElementException:					 		
			log.exception('Element ' + name_element + ' not found');		
		except AttributeError:
			pass
		
		time.sleep(0.5)


		try:
			suggest_tabs_in = self.driver.find_element_by_class_name(suggest_tabs)		
			log.info('Element ' + suggest_tabs + ' found')					
			log.info('Suggest displayed: {}'. format(suggest_tabs_in.is_displayed()))	
		except NoSuchElementException:								
			log.exception('Element ' + suggest_tabs + 'not found');

		try:
			self.search_form.submit()
		except AttributeError:
			pass 
		
	'''
	//////////////////////////////////////////////////////////////////////////////////////////////
	Function: search the 'search bar' by xpath, enter a query into the 'search bar', checking the
	display of the suggest table on the page, with the result being entered in the logs.
	///////////////////////////////////////////////////////////////////////////////////////////////			
	'''


	def link_search(self, url, try_name_elements, except_name_elements, amount):
		try:
			links = self.driver.find_elements_by_xpath(try_name_elements)	
		except:
			links = self.driver.find_elements_by_xpath(except_name_elements)		
		results_search_links = []
		number = 0
		for link in links[:amount]:
			href = link.get_attribute("href")
			results_search_links.append(href)
		matching_with = [i for i in results_search_links if url in i]
		if len(matching_with) > 0:
			log.info (' URL is in {} links:\n {}'. format(len(matching_with), matching_with))
		else:
			log.info ('Not URL in page')
	'''
	//////////////////////////////////////////////////////////////////////////////////////////
	The function of checking the search results for compliance with this link, with the
	entry result in logs.
	//////////////////////////////////////////////////////////////////////////////////////////		
	'''

	def url_equal_link(self, link):
		if self.driver.current_url == link:
			log.info( 'URL equally {}'. format(link))

		else: log.info( 'URL not equally {}'. format(link))
	'''
	///////////////////////////////////////////////////////////////////////////////////////
	The function of checking the correspondence of the address bar and this link with the
	entry result in logs.
	//////////////////////////////////////////////////////////////////////////////////////			
	'''

			
	def click_system (self, choice_search, name_button):
		if choice_search == 0:
			time.sleep(0.5)
			try:
				self.search_class(name_button).click()
			except AttributeError:
				pass				
		elif choice_search == 1:
			time.sleep(0.5)
			try:
				self.search_xpath(name_button).click()
			
			except AttributeError:
				pass
	'''
	//////////////////////////////////////////////////////////////////////////////////////	
	Click Simulation Function.
	//////////////////////////////////////////////////////////////////////////////////////			
	'''


	def quit (self):
		log.info('{}   closed in {}'. format(self.driver, log_time) + '\n' * 4)
		time.sleep(1)
		self.driver.quit()
	

	'''
	//////////////////////////////////////////////////////////////////////////////////////
	Quit function.
	//////////////////////////////////////////////////////////////////////////////////////			
	'''



	

