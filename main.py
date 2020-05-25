from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


# sign in page
@app.route('/sign_in')
def sign_in_page():
    return 'Sign in here!'


# overview of algorithms
@app.route('/algorithms')
def algorithms_page():
    return 'algorithms page'


# upload data page
@app.route('/upload_data')
def upload_data_page():
    return 'Upload data here!'


# preprocessing page
@app.route('/preprocessing')
def preprocessing_overview_page():
    return 'Preprocess your data here!'


# report page
@app.route('/feedback_report')
def report_page():
    return 'Here you can find the report'