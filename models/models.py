import pymysql
from flask_sqlalchemy import SQLAlchemy

from app import app
from sqlalchemy import *

pymysql.install_as_MySQLdb()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/e_album'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
