# pokereye
server for image recognition

To install the server:
 $ virtualenv venv
 $ . venv/bin/activate
 $ python server.py

filesystem:
html pages are in templates/
css in static/
python code in /
uploaded files in /uploads

sitemap and routes:
/, /index.html          => templates/upload.html
/upload (POST)          => templates/success.html
/last_file              => uploads/{{ last uploaded filename}}
/uploads/{{ filename }} => uploads/{{ filename }}

