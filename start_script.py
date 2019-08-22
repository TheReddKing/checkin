from app.app import app, db
from app.models import *
import sys

if(User.query.filter(User.username == app.config["ADMIN_USERNAME"]).count() == 0):
    admin = User(app.config["ADMIN_USERNAME"],
                 app.config["ADMIN_PASSWORD"], 'HackMIT Admin', True)
    db.session.add(admin)
    db.session.commit()
