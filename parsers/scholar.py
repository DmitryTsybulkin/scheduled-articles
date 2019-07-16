from bs4 import BeautifulSoup
import requests

class Scholar(object):
	# URL https://scholar.google.ru/scholar?scisbd=2&q=quantum+theory&hl=en&as_sdt=0,5
	site = 'https://scholar.google.ru/'
	page_number = 0
	tags = []

	def __init__(self, tags):
		self.tags = tags
		# self.query += 'scholar?start=0&scisbd=2&q=' + self.tagsToStringForQuery(tags) + '&hl=en&as_sdt=0,5'
		print("Class parser for scholar site created!")

	def generateQuery(self, page_number):
		return 'scholar?start=' + str(page_number - 1) + '0&scisbd=2&q=' + self.tagsToStringForQuery() + '&hl=en&as_sdt=0,5'

	def getURL(self, page_number):
		return self.site + self.generateQuery(page_number)

	def tagsToStringForQuery(self):
		result = ''
		lenghtListTags = len(self.tags)

		for i in range(lenghtListTags):
			result += self.tags[i].replace(" ", "+")
			if(i != lenghtListTags - 1):
				result += ',+'

		return result

	def parsing(self):
		page = requests.get(self.getURL(1))

		if(page.status_code != 200):
			print("Error loading page")
			return None
		
		soup = BeautifulSoup(page.text, 'html.parser')

		articles = soup.find_all('div', class_='gs_ri')

		result = []
		for article in articles:
			# print(article.select('.gs_rt a')[0].getText())
			result.append(article.select('.gs_rt a')[0].getText())

		return result

