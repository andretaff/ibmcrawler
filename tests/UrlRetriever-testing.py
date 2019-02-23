import unittest
import UrlRetriever

class TestUrlRetriever(unittest.TestCase):
	def test_retrieveUrl(self):
		cUrlRetriever = UrlRetriever.tUrlRetriever('http://www.fakeurl',0)
		mLinks = cUrlRetriever.retrieveURLLinks()
		self.assertTrue(mLinks == {})
		
		cUrlRetriever = UrlRetriever.tUrlRetriever('http://www.google.com',0)
		mLinks = cUrlRetriever.retrieveURLLinks()
		self.assertFalse(mLinks == {})
		for sLink, iDepth in mLinks.items():
			print ('Retrieved',sLink)
			self.assertTrue(sLink.startswith('http'))
			self.assertTrue(iDepth>=0)

if __name__ == '__main__':
    unittest.main()