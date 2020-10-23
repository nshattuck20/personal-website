from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def index(): 
	return render_template('templates/static/index.html')

@app.route('/about/')
def about():
	return 'The about page'

# enables ability to run 'python file_name in terminal'
if __name__ == '__main__':
	app.run(debug=True)


'''
 - Enable all development features (including debig mode) with FLASK_ENV environmentn variable. 
 - Set to development before running the server. 

 $ export FLASK_ENV=development
 $ flask run

 - Activates debugger 
 - Activates automatic reloader 
 - Enables debug mode of flask app
'''