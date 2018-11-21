# coding=utf-8
from flask import request
from app import app
from app.schet_maker import schet_maker
import json

app.config['SECRET_KEY'] = ''

@app.route('/', methods=['POST'])
def result():
    if request.method == 'POST':
        result = request.form
        data = result.to_dict()
        for k, v in data.items():
            data[k] = v.encode().decode()
        with open('_.json', 'w') as f:
            json.dump(data, f)
        dogs_n_nmnkltrs = schet_maker(result.to_dict())
        if dogs_n_nmnkltrs:
            return dogs_n_nmnkltrs
        else:
            return 'error!'
    return 'smth went wrong'