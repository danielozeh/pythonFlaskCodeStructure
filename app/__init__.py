from flask import Flask
import os

from app.user.views import user_blueprint
from app.admin.views import admin_blueprint

app = Flask(__name__)

app.secret_key = 'mynameisDanielandIamASoftwareDeveloper'

#REGISTER USER BLUEPRINT
app.register_blueprint(user_blueprint, url_prefix='/')

#REGISTER ADMIN BLUEPRINT
app.register_blueprint(admin_blueprint, url_prefix='/admin')