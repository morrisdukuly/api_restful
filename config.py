from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEY'] = "asus"

#==========================================================Connexion de la base de donnee SQLAlchemy===================================================================

app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:@localhost/order-dba" #formatage


#connexion a la base de donnee

db = SQLAlchemy(app)
#===========================================================================
