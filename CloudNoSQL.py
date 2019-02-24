import os
import json
from cloudant.client import Cloudant

class tCloudNoSQL:
	def __init__(self):
		self.databaseName = 'ibmtest'
		if 'VCAP_SERVICES' in os.environ:  #connect uing cloud variables
			vcap_servicesData = json.loads(os.environ['VCAP_SERVICES'])
			cloudantNoSQLDBData = vcap_servicesData['cloudantNoSQLDB']
			credentials = cloudantNoSQLDBData[0]
			credentialsData = credentials['credentials']
			self.serviceUsername = credentialsData['username']
			self.servicePassword = credentialsData['password']
			self.serviceURL = credentialsData['url']
		else: #connect using static parameters
			self.serviceUsername = 'a2dcc013-e43e-4824-aca7-30810c73d11a-bluemix'
			self.servicePassword = '83a575e3a08675e55ce75f1c433d0666913d1b177fcbe59b91ee68c5e646b529'
			self.serviceURL = 'https://a2dcc013-e43e-4824-aca7-30810c73d11a-bluemix:83a575e3a08675e55ce75f1c433d0666913d1b177fcbe59b91ee68c5e646b529@a2dcc013-e43e-4824-aca7-30810c73d11a-bluemix.cloudantnosqldb.appdomain.cloud'
	def connect(self):
		self.client = Cloudant(self.serviceUsername, self.servicePassword, url=self.serviceURL)
		self.client.connect()
		self.myDatabase = self.client[self.databaseName]
		if self.myDatabase.exists():
			print ('Database connected',self.databaseName)
		else:
			print ('Error connecting',self.databaseName)
	
	def saveDocument(self,data):
		self.myDatabase.create_document(data)
	
	def retrieveDocuments(self):
		result = []
		try:
			for document in self.myDatabase:
				result.append(document)
		except:
			pass #avoid error in py 3.7
		return result
	
	def deleteAllDocuments(self):
		try:
			for document in self.myDatabase:
				document.delete()
		except:
			pass #avoid error in py 3.7