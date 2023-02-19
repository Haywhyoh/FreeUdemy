import requests
import time
import json
category = "IT+%26+Software"
header = {
  "Accept": "application/json, text/plain, */*",
  "Authorization": "Basic TDgwQzhqdm1lcEtraVVrNDdDSjEzcklhMGVWMEdERDVoVXJOV0xIeTpOZEVRWUhNbVBhUVdXMm9DRE5hZ3JMTUxhWXRZZEdZcU1GU3lXNDRldUYxZUVmRmNidklnc3BqZDF1cUt1WTR1cDk1ME9YaERYZnM5Q3JNbjhwbENIeVNxVkVFSVZodGp6MlZVVXB6MFh6WXpBZkx0b3dOb2FYQ1A1SGtqQm9hUw==",
  "Content-Type": "application/json"
}
course_list = []
for i in range(1, 24):
    
    page_num = i
    url = "https://www.udemy.com/api-2.0/courses/?category={}&page={}&page_size=100&price=price-free".format(category, page_num)
    response = requests.get(url, headers=header).json()
    if response is None:
        break
    if "results" not in response.keys():
        break
    courses = response["results"]
    for course in courses:
        course_list.append(course)
    time.sleep(10)
    print(len(course_list))
with open("../models/software.json", "w") as fp:
    course_json = json.dump(course_list, fp)