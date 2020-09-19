import requests
from SafepalDjangoBackend.settings import env


def upload_video(title, description, category_id, thumbnail, video):
    data = {
        "category_id": category_id,
        "title": title,
        "description": description,
        "rating": 5,
        "duration": 1
    }

    files = [
        ("thumbnail", open(r'' + thumbnail, 'rb')),
        ("url", open(r'' + video, 'rb'))
    ]

    req = requests.post(url=env('BASE_URL') + "/api/v1/videos", files=files, data=data)
    print(req.status_code)
    print(req.content)
