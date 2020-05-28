from Algorithm import *

from flask import Flask
from flask import render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


@app.route('/')
def hello_world():
    return render_template('home2.html', title="Home")
    # NOTE:: changed to home2 for now


# sign in page
@app.route('/sign_in')
def sign_in_page():
    return render_template('sign_in2.html', title="Sign in")
    # NOTE:: changed to sign_in2 for now


# overview of algorithms
@app.route('/algorithms')
def algorithms_page():
    return render_template('algorithms.html', title="Algorithms", algorithms=get_algorithms())


# upload data page
@app.route('/upload_data')
def upload_data_page():
    return render_template('upload_data.html', title="Upload data")


# preprocessing page
@app.route('/preprocessing')
def preprocessing_overview_page():
    return render_template('preprocessing.html', title="Preprocessing")


# report page
@app.route('/feedback_report')
def report_page():
    return render_template('feedback_report.html', title="Feedback Report")


# profile page
@app.route('/profile')
def profile_page():
    return render_template('profile.html', title="Profile")