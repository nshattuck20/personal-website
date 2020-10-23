from flask import Flask 


# bind a function to a URL

@app.route('/hello')
def hello_world():
	return 'Hello, world!'

