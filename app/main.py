from flask import Flask, render_template


app = Flask(__name__)


posts = [
            {
                'author': 'Omar Akhman',
                'title': 'Mahz Mahnz',
                'content': 'In the begining ....',
                'date_posted': '16 July, 2021'
            },
            {
                'author': 'Uuhm Oi',
                'title': 'Mahz',
                'content': 'In the end ....',
                'date_posted': '16 July, 2021'
            }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
