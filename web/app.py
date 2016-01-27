# app.py

import socket

from flask import Flask
from flask import request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from models import *


@app.route('/', methods=['GET', 'POST'])
def index():
    template_data = {}
    if request.method == 'POST':
        text = request.form['text']
        post = Post(text)
        db.session.add(post)
        db.session.commit()
    template_data["posts"] = Post.query.order_by(Post.date_posted.desc()).all()
    template_data["hostname"] = socket.gethostname()
    return render_template('index.html', **template_data)


if __name__ == '__main__':
    app.run()
