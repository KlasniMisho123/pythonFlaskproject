from flask import Flask, render_template, url_for, flash, redirect
from forms import Registrationform, Loginform
import secrets

secret_number = secrets.token_hex(16)
app = Flask(__name__)

app.config["SECRET_KEY"] = "77a486f0f65c2ab0a38810c5a206def4"

posts = [
    {
        "author": "Misho Silagava",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "May 31, 2023"
    },
    {
        "author": "Corey Schafer",
        "title": "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "June 1, 2023"
    },
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
    form = Registrationform()
    if form.validate_on_submit():
        flash(f"Accaunt Created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = Loginform()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You Have Been Logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Unseccesfull login!", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)

print("btu")