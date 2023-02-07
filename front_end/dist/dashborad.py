from flask import Flask, render_template, url_for
import requests
import json

app = Flask(__name__)
# headers = {
#   "Accept": "application/json, text/plain, */*",
#   "Authorization": "Basic TDgwQzhqdm1lcEtraVVrNDdDSjEzcklhMGVWMEdERDVoVXJOV0xIeTpOZEVRWUhNbVBhUVdXMm9DRE5hZ3JMTUxhWXRZZEdZcU1GU3lXNDRldUYxZUVmRmNidklnc3BqZDF1cUt1WTR1cDk1ME9YaERYZnM5Q3JNbjhwbENIeVNxVkVFSVZodGp6MlZVVXB6MFh6WXpBZkx0b3dOb2FYQ1A1SGtqQm9hUw==",
#   "Content-Type": "application/json"
# }
# response = requests.get("https://www.udemy.com/api-2.0/courses/?page=1&page_size=10", headers=headers).json()
# courses = response["results"]

categories = ["Business", "Design", "Development", "Finance & Accounting", "Health & Fitness", "IT & Software", "Lifestyle", 
                "Marketing", "Music", "Office", "Productivity", "Personal Development",
                "Photography & Video", "Teaching & Academics"]

with open("/Users/macbook/Documents/Personal_Projects/Web-Dev /FreeUdemy/data.json") as file:
    response = json.load(file)

courses = response["results"]


@app.route('/courses', strict_slashes=False)
def courses_route():
    return render_template('courses.html', courses=courses,  categories = categories)

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    new_list = courses[:6]
    return render_template( 'index.html', courses=new_list,  categories = categories)

@app.route('/login',  strict_slashes=False )
def login():
    return render_template('login.html')

@app.route('/signup',  strict_slashes=False )
def signup():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(port=5500, debug=True)
