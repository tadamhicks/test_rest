from flask import Flask, request, session, redirect, url_for, jsonify, make_response
import json

DEBUG = True
SECRET_KEY = 'akduiqheacda'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.json.get('name')
        size = request.json.get('size')
        with open('results.txt', 'w') as f:
            f.write(name + '\n')
            f.write(size + '\n')
        return make_response(jsonify({'SUCCESS': 'success'}), 200)
    if request.method == 'GET':
        name = 'adam'
        size = 'XL'
        return jsonify(name=name, size=size)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5555)
