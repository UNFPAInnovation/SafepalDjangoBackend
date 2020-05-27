# Safepal Django Backend
Safepal Django Backend handles GBV content in the Safepal app. That is videos, articles, quiz, questions


## Installation
The requirements depend on some system components. Please install the following
- sudo apt install redis-server
- sudo apt install ffmpeg

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements


## Resources
- https://docs.google.com/document/d/1qzEvukm5osJsfB-pEkBbgF_zlyULxNzluBd2YCAXsqo/edit (requires access)
- https://www.revsys.com/tidbits/how-add-django-models-wagtail-admin/
- https://docs.wagtail.io/en/v2.1.1/getting_started/integrating_into_django.html
- https://github.com/axnsan12/drf-yasg
- https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04


## Usage
| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| GET | / | Access to the api documentation|
| GET | /cms | CMS dashboard used to edit the GBV content |
| GET | /admin | Access to the developer dashboard |

&copy;safepal