from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)
headers = {
  "Accept": "application/json, text/plain, */*",
  "Authorization": "Basic TDgwQzhqdm1lcEtraVVrNDdDSjEzcklhMGVWMEdERDVoVXJOV0xIeTpOZEVRWUhNbVBhUVdXMm9DRE5hZ3JMTUxhWXRZZEdZcU1GU3lXNDRldUYxZUVmRmNidklnc3BqZDF1cUt1WTR1cDk1ME9YaERYZnM5Q3JNbjhwbENIeVNxVkVFSVZodGp6MlZVVXB6MFh6WXpBZkx0b3dOb2FYQ1A1SGtqQm9hUw==",
  "Content-Type": "application/json"
}
response = requests.get("https://www.udemy.com/api-2.0/courses/?page=1&page_size=10", headers=headers).json()
courses = response["results"]

@app.route('/overview', strict_slashes=False)
def dashboard():
    return render_template('overview.html')

@app.route('/courses', strict_slashes=False)
def courses_route():
    return render_template('courses.html', courses=courses)

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    new_list = []
    for course in courses:
        if course['id'] >= 50000:
            new_list.append(course)
    return render_template( 'index.html', courses=new_list)

@app.route('/login',  strict_slashes=False )
def login():
    return render_template('login.html')

@app.route('/signup',  strict_slashes=False )
def signup():
    return render_template('signup.html')

@app.route('/course_page', strict_slashes=False)
def course_page():
    return render_template('course_page.html', courses=courses)

@app.route('/checkout', strict_slashes=False)
def cart_page():
    return render_template('checkout.html')

if __name__ == "__main__":
    app.run(port=5500, debug=True)
