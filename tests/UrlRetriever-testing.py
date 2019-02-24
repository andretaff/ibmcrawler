import unittest
import UrlRetriever

class TestUrlRetriever(unittest.TestCase):
	def test_retrieveFakeUrl(self):
		cUrlRetriever = UrlRetriever.tUrlRetriever('http://www.fakeurl',0)
		mLinks = cUrlRetriever.retrieveURLLinks()
		self.assertTrue(mLinks == {})

	def test_emptywebpage(self):
		cUrlRetriever = UrlRetriever.tUrlRetriever('http://hmpg.net/',3) #The end of the internet webpage
		mLinks = cUrlRetriever.retrieveURLLinks()
		self.assertTrue(mLinks == {})

	def test_retrieveUrl(self):
		cUrlRetriever = UrlRetriever.tUrlRetriever('http://www.google.com',0)
		mLinks = cUrlRetriever.retrieveURLLinks()
		self.assertFalse(mLinks == {})
		for sLink, iDepth in mLinks.items():
			self.assertTrue(sLink.startswith('http'))
			self.assertTrue(iDepth>=0)

if __name__ == '__main__':
    unittest.main()