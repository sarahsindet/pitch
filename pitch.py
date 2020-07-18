from flask_bootstrap import Bootstrap
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Sarah Sindet',
        'title': 'Pitch post 1',
        'content': 'First post content',
        'date_posted': 'July 17, 2020'
    },
    {
        'author': 'Daniel Sindet',
        'title': 'Pitch post 2',
        'content': 'Second post content',
        'date_posted': 'July 18, 2020'
    }    
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)
    

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug = True)    