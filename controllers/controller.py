from app import app

from flask import render_template

from app.models.guitar_list import guitars

@app.route('/')
def index():
    return render_template('index.html', title='Home', guitars=guitars) 


