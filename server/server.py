#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, send_from_directory
from werkzeug import secure_filename

# Initialize the Flask application
app = Flask(__name__,  static_url_path='/static')


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/update/<msg>")
def update(msg):
    return render_template('update.html', msg=msg)


@app.route('/upload')
def render_file():
    return render_template('upload.html')


@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 + 파일명
        f.save(secure_filename(f.filename))
        return '업로드 성공'


@app.route('/download',  methods=["GET", "POST"])
def download():
    uploads = "files"
    return send_from_directory(directory=uploads, filename="1.1.zip")


@app.route("/version")
def version():
    if os.path.isfile(r'static/version.txt'):
        f = open(r'static/version.txt', 'r')
        GetVersionFromFile = f.read().replace('\n', '').strip()
    return GetVersionFromFile


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
