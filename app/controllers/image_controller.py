from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app import app
from app.models.image_model import save_image, get_all_images
import os
import uuid

# Check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@app.route('/')
def index():
    # Fetch all images from the database
    images = get_all_images()
    return render_template('upload.html', images=images)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']

    if file.filename == '':
        return "No selected file", 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
         # Generate a unique identifier using uuid and combine it with the original filename
        unique_filename = str(uuid.uuid4()) + "_" + filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)

        # Save the file to the static folder
        file.save(file_path)

        # Insert image filename into the database
        save_image(unique_filename)

        return redirect(url_for('index'))

    return "File not allowed", 400
