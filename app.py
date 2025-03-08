from flask import Flask
from config import db, migrate
from routes.user import user_bp
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager

#cargar variables de entorno
load_dotenv()

app=Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY']='wyhgewty3g278te62fec32uhes'
jwt=JWTManager(app)

#configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#inicializar extensiones
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(user_bp, url_prefix='/users')

if __name__=='__main__':
    app.run(debug=True)