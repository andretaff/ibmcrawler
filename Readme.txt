################################################
#											   #
#	 	  IBM Test Crawler Application		   #
#				André Taffarello			   #
#											   #
################################################

- GitHub repository: https://github.com/andretaff/ibmcrawler

- Content:
	- ibmcrawler.py - main file
	- URLRetriever.py - class used to retrieve and process web pages
	- CloudNoSLQ.py - class used for database access (cloudant)
	- Requiremets.txt - modules needed for this project
	- manifest.yml - manifest file for ibm cloud
	- Procfile - command line setting for ibm cloud
	- runtime.txt - Python requirement for this project
	/ templates
		- index.html - main webpage (python flask)
		- results.html - results page
	/tests
		- UrlRetriever-testing.py - unit testing of that class
		- CloudNoSLQ-testing.py - unit testing f that class
		

- Using the app (python >= 3.6 required)
	- Local: 
		$ pip install -r requirements.txt
		$ python ibmcrawler.py
		access http://localhost:8000/ using Chrome
	- Cloud:
		access http://ibmtestcrawler.mybluemix.net/
	
	Either way, ibm cloudant database is used to store and retrieve saved links
	
- Parameters
	- URL to retrieve
	- Max Depth to go further (0 only looks the first webpage, 1 looks inside the links found on that webpage, 2 goes further recursively)
	
	
- Testing
	$ python unittest -m tests\UrlRetriever-testing.py
	--------------------------------------------------
	$ python unittest -m tests\CloudNoSLQ-testing.py
	
	