import requests
import os

BASE_URL = "https://testwebdashboard.safepal.co"

def uploadVideo(title, description, category_id, thumbnail, video):
	data = {
	    "category_id": 1,
	    "title": title,
	    "description": description,
	    "rating": 5,
	    "duration": 1
	}

	files = [
		("thumbnail", thumbnail = open(r'' + thumbnail, 'rb')),
	    ("url", video = open(r'' + video, 'rb'))
	]

	req = requests.post(url=BASE_URL + "/api/v1/videos", files=files, data=data)
	print(req.status_code)
	print(req.content)