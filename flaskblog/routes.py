from flask import render_template, url_for, flash, redirect

import flaskblog.Data.rap
import flaskblog.Data.rock
import flaskblog.Data.pop
from flaskblog import app, db, bcrypt
from flaskblog.forms import Registrationform, Loginform
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user


posts = [
    {
        "title": "Pop",
        "image": "static/Photos/pop2.png",
    },
    {
        "title": "Rap",
        "image": "static/Photos/rapper.png",
    },

    {
        "title": "Rock",
        "image": "static/Photos/rock.png",
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title="About", )


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = Registrationform()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You are now able to log in {form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = Loginform()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("home"))
        else:
            flash("Unseccesfull login. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/account')
def account():
    return render_template("account.html", title="Account")


@app.route('/Pop', methods=["GET", "POST"])
def pop():
    if current_user.is_authenticated:
        return render_template("pop.html", title="Top25 Pop Music", pops=flaskblog.Data.pop.pop_music)
    else:
        return redirect(url_for("register"))


@app.route('/Rap', methods=["GET", "POST"])
def rap():
    if current_user.is_authenticated:
        return render_template("rap.html", title="Top25 Rap Music", raps=flaskblog.Data.rap.rap_music)
    else:
        return redirect(url_for("register"))


@app.route('/Rock', methods=["GET", "POST"])
def rock():
    if current_user.is_authenticated:
        return render_template("rock.html", title="Top25 Rock Music", rocks=flaskblog.Data.rock.rock_music)
    else:
        return redirect(url_for("register"))



""" errori akvs """
