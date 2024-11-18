import os
from werkzeug.utils import secure_filename
from app.config.mysqlconnection import connectToMySQL  
from app import app

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = os.path.join('app', 'static', 'images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Database connection setup using the connectToMySQL function
def save_image(filename):
    query = "INSERT INTO image (img) VALUES (%(img)s)"
    data = {"img": filename}
    db = connectToMySQL(app.config['DATABASE'])  
    return db.query_db(query, data)

def get_all_images():
    query = "SELECT id, img FROM image"
    db = connectToMySQL(app.config['DATABASE'])
    return db.query_db(query)
