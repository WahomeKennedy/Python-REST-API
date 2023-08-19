import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "video/2", {"views": 99, "likes": 103})
print(response.json())