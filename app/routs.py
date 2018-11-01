# coding=utf-8
from flask import request
from app import app

app.config['SECRET_KEY'] = 'gshn'


@app.route('/', methods=['POST'])
def result():
    if request.method == 'POST':
        result = request.form
        print(result)
        return 'OK'
    return 'Received !'

# docker build . -t flask-app &
# docker run -d -p 81:81 --name gshn flask-app
# docker exec -ti gshn /bin/sh
