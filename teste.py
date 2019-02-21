from flask import Flask, request,render_template
import UrlRetriever

app = Flask(__name__, static_url_path='')

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
	url = request.form['text']
	cUrlRetriever = UrlRetriever.tUrlRetriever(url,3)
	mLinks = cUrlRetriever.retrieveURLLinks()
	for sUrl,iDepth in mLinks.items():
		print (sUrl,iDepth)
	
	print ('End')
	
if __name__ == '__main__':
    app.run()
	