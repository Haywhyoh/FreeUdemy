from flask import Flask, render_template, url_for, request, flash, redirect, session
from flask_session import Session
from flask_login import login_user, logout_user, login_required, current_user
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from models import users
from models.engine.db_storage import DBStorage

db = DBStorage()
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

courses = requests.get("http://127.0.0.1:5000/api/v1/courses/?query=&categories=courses").json()
categories = [{"All_Categories" : "courses"}, {"Design" : "design"} , {"Development" : "development"}, {"Finance_Accounting" : "finance"}, {"Health_Fitness" : "health"}, {"IT&Software" : "software"}]


@app.route('/courses', strict_slashes=False)
def courses_route():
    return render_template('courses.html', courses=courses,  categories = categories)

@app.route('/search/', strict_slashes=False,)
def search_route():
    category = request.args.get('categories')
    query = request.args.get('queries')
    course_list = requests.get("http://127.0.0.1:5000/api/v1/courses/?query={}&categories={}".format(query, category)).json()
    return render_template('courses.html', courses=course_list,  categories = categories)
 
@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    return render_template( 'index.html', courses=courses,  categories = categories)

@app.route('/login', methods=['GET', 'POST'], strict_slashes=False )
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = db.get_user(users, username)
        if user:
            if check_password_hash(user['password'], password):
                session["logged_in"] = True
                session["username"] = username
                flash("Logged in!", category='success')
                return redirect(url_for('home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('username does not exist.', category='error')

    return render_template("add_course.html", user=current_user)

@app.route('/signup',  methods=['GET', 'POST'], strict_slashes=False )
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user = db.get_user(users, username)

        if user:
            email_exists = user["email"]
            username_exists = user["username"]
            if email_exists:
                flash('Email is already in use.', category='error')
            elif username_exists:
                flash('Username is already in use.', category='error')
            elif password1 != password2:
                flash('Password don\'t match!', category='error')
            elif len(username) < 2:
                flash('Username is too short.', category='error')
            elif len(password1) < 6:
                flash('Password is too short.', category='error')
            elif len(email) < 4:
                flash("Email is invalid.", category='error')
        else:
            new_user = db.add_user(collection=users, email=email, username=username, password=generate_password_hash(
            password1, method='sha256'))
            session['logged_in'] = True
            flash('User created!')
            session['new_user'] = new_user
            return redirect(url_for('/courses_route'))

    return render_template("signup.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(port=5500, debug=True)
