from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ananth Vankipuram'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'A beautiful day in San jose'
            
        },
        {
            'author': {'username':'Susan'},
            'body':'The avengers movie was cool'
        },
        
        
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)