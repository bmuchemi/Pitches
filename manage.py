from app import create_app,db
from app.models import User
from flask_script import Manager, Server

app = create_app('prod')

