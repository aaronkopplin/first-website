from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'aaron kopplin',
        'title' : 'blog post 1',
        'content' : 'first post content',
        'date_posted' : 'April 1, 2020'
    },
    {
        'author' : 'jane doe',
        'title' : 'blog post 2',
        'content' : 'second post content',
        'date_posted' : 'April 2, 2020'
    }
]

@app.route("/")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
