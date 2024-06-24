from flask import render_template, redirect, url_for, request
from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        post = {
            'name': request.form['name'],
            'city': request.form['city'],
            'hobby': request.form['hobby'],
            'age': request.form['age'],
            'title': request.form['title'],
            'content': request.form['content']
        }
        posts.append(post)
        return redirect(url_for('index'))
    return render_template('blog.html', posts=posts)