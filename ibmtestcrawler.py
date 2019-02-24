from flask import Flask, request,render_template
import UrlRetriever
import os
import CloudNoSQL

app = Flask(__name__, static_url_path='')
cDatabase = CloudNoSQL.tCloudNoSQL()

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
	url = request.form['url']
	depth = 0
	try:
		depth = int(request.form['depth'])
	except:
		depth = 2
	if depth>3:
		depth = 2
		
	depth = depth - 1
	print('Depth',depth)
		
	cDatabase.deleteAllDocuments()
	cUrlRetriever = UrlRetriever.tUrlRetriever(url,depth)

	mLinks = cUrlRetriever.retrieveURLLinks()
	cDatabase.saveDocument(mLinks)
	mList = cDatabase.retrieveDocuments()
	items = []
	for item in mList:
		for sUrl,iDepth in item.items():
			if sUrl not in ('_id','_rev'):
				items.append([sUrl,iDepth])
	items = sorted(items, key=lambda item: item[1]) 
	return render_template("result.html", url=url,depth=depth+1, result = items)
	
if __name__ == '__main__':
	port = int(os.getenv('PORT', 8000))
	
	cDatabase.connect()
	app.run(host='0.0.0.0', port=port)	