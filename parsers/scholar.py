from bs4 import BeautifulSoup
import requests
import calendar
import datetime
import time

class Scholar(object):
	# URL https://scholar.google.ru/scholar?scisbd=2&q=quantum+theory&hl=en&as_sdt=0,5
	site = 'https://scholar.google.ru/'
	page_number = 0
	tags = []

	def __init__(self, tags):
		self.tags = tags
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
		currentDate = datetime.datetime.now()
		countDayCurrentMonth = calendar.monthrange(currentDate.year, currentDate.month)[1]

		run = True
		numberPage = 1
		listArticles = []
		print('Parser start')
		while run:
			page = requests.get(self.getURL(numberPage))
			# print("===== HTML PAGE =====")
			# print(page)
			
			soup = BeautifulSoup(page.text, 'html.parser')
			# print("===== BS4 HTML =====")
			# print(soup)

			articles = soup.find_all('div', class_='gs_ri')
			# print("===== ARTICLES =====")
			# print(articles)
			# break

			result = []
			for article in articles:
				# print(article)
				spanTagWithDate = article.select('.gs_rs span')

				if(spanTagWithDate == []):
					continue

				publicDate = spanTagWithDate[0].getText().split()

				if(int(publicDate[0]) > countDayCurrentMonth):
					run = False
					break
				
				titleArticle = article.select('.gs_rt a')[0].getText()
				href = article.select('.gs_rt a')[0].attrs['href']
				# print(titleArticle)
				# print(href)

				# listArticles.append({'titleArticle': titleArticle, 'href': href})
				result.append({'titleArticle': titleArticle, 'href': href})
			
			print('=================================================================================')
			print('Page number ' + str(numberPage))
			print(result)
			result = []

			numberPage += 1
			time.sleep(3)

		return listArticles
		# page = requests.get(self.getURL(1))

		# if(page.status_code != 200):
		# 	print("Error loading page")
		# 	return None
		
		# soup = BeautifulSoup(page.text, 'html.parser')

		# articles = soup.find_all('div', class_='gs_ri')

		# result = []
		# for article in articles:
		# 	result.append(article.select('.gs_rt a')[0].getText())

		# return result

