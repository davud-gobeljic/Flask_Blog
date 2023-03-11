from flask import Flask, render_template, url_for
app = Flask(__name__)
# app.debug = True

posts = [

    {
        'author': 'Corey Shafer',
        'title':  'Blog post 1',
        'content': 'First blog content',
        'date_posted': 'April 20, 2022',

    },

    {
        'author': 'John Doe',
        'title':  'Blog post 2',
        'content': 'Second blog content',
        'date_posted': 'August 20, 2022'

    }
]

@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)



