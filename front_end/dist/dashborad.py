from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__)
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

@app.route('/login',  strict_slashes=False )
def login():
    return render_template('login.html')

@app.route('/signup',  strict_slashes=False )
def signup():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(port=5500, debug=True)
