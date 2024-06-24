from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test_key_for_testing'

from app import routes
