# UrlRetriever.py
# - a simple class designed to, given a particular url, retrieve all links inside that webpage text
# - method retrieveURLLinks returns a map with pairs url,depth found

from bs4 import BeautifulSoup
import requests
import copy
from urllib.parse import urlparse

class tUrlRetriever:
	def __init__(self, sURL, iDepth):
		self.sURL = sURL
		self.iDepth = iDepth
		self.mLinks = {}
	
	def recursivelyRetrieveURLLinks(self, sCurrentURL, iCurrentDepth):
		#internal recurive function
		if (sCurrentURL == ''):
			return
		print ('now retrieving: ',sCurrentURL,self.iDepth-iCurrentDepth)
		try:
			cPage = requests.get(sCurrentURL)
		except:
			print ('ERROR RETRIEVING ',sCurrentURL)
			return
		cSoup =	BeautifulSoup(cPage.content, 'html.parser')
		lLinks = []
		parsed = urlparse(sCurrentURL)
		dominio =  '{uri.scheme}://{uri.netloc}'.format(uri=parsed)

		for link in cSoup.find_all('a'): #get all links
			sHref = str(link.get('href'))
			if sHref.startswith('http'): #but only starting with http
				lLinks.append(sHref)
			elif sHref.startswith('/'):  #or / (links within same domain)
				lLinks.append(dominio + sHref)
			
		for link in lLinks: # go throgh all the links
			if not link in self.mLinks: #get all the new ones
				self.mLinks[link] = self.iDepth-iCurrentDepth+1 #add it
				if iCurrentDepth>0:
					self.recursivelyRetrieveURLLinks(link,iCurrentDepth-1) #and go inside it again if needed
	
	def retrieveURLLinks(self):
		self.recursivelyRetrieveURLLinks(self.sURL,self.iDepth)
		return copy.deepcopy(self.mLinks)
		