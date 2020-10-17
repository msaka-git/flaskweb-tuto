from flask import render_template, url_for, flash, redirect
from deneme_flask.forms import RegistrationForm, LoginForm
from deneme_flask import app, db, bcrypt
from deneme_flask.modules import User,Post
from flask_login import login_user, current_user,logout_user


posts = [

    {
        'author': 'Hamdullah Suphi',
        'title': 'Sonbahar',
        'content': 'Ilk post',
        'date_posted': 'April 20, 2018'

    },

    {
        'author': 'Anil Dursun',
        'title': "Paris'te Hayat",
        'content': 'Deneme Yazilari',
        'date_posted': 'May 23, 2017'


    }


]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)



@app.route("/about")
def about():

    return render_template('about.html', title='About')





@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login unseccessful. Please check your data', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

