from flask import Flask, render_template, url_for


app = Flask(__name__)

posts = [
    {
        'author': 'Nick Shattuck',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 21, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


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
