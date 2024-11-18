from flask import Flask

app = Flask(__name__)
app.secret_key = "secret_key"

app.config['DATABASE'] = "saveIMG"

from app.controllers.image_controller import *
