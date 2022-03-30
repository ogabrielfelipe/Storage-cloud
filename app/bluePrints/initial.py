from app import app
from flask import render_template


@app.route('/', methods=['GET'])
def root_send_file():
    return render_template('index.html')
