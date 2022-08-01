#!/usr/bin/env python3
from flask import (
    Flask,
    render_template,
    flash,
    url_for,
    redirect
)
from forms import LoginForm, RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '80149b55cdee8f6763268121b0f51e73'


posts = [
    {
        'author': 'Author 1',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Last post date posted',
    },
    {
        'author': 'Author 2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Last post date posted',
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and \
            form.password.data == 'password':
            flash(f'You have been logged in !', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login failed. Check your creds.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
