import unittest
import CloudNoSQL

class TestCloudDatabase(unittest.TestCase):
	def setUp(self):
		self.document = { "test": 0}
		self.myDatabase = CloudNoSQL.tCloudNoSQL()
		self.myDatabase.connect()
		
	def test_deleteAllDocs(self):
		self.myDatabase.deleteAllDocuments()
		result = self.myDatabase.retrieveDocuments()
		self.assertTrue(result == [])
	
	def test_saveDocument(self):
		self.myDatabase.saveDocument(self.document)
		newDoc = self.myDatabase.retrieveDocuments()
		self.assertTrue(len(newDoc)>0)
		newDoc = newDoc[0]
		self.assertTrue(newDoc['test']==self.document['test'])
	
if __name__ == '__main__':
    unittest.main()