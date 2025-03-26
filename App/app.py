from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configurações do upload da imagem
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Função para verificar se o arquivo é permitido
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Valores iniciais para ajustes
settings = {
    "brightness": 1.0,
    "contrast": 1.0,
    "blur": 0,
    "saturation": 1.0,
    "sepia": 0.0,
    "grayscale": 0.0,
    "image_url": None
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Verifica se o usuário enviou um arquivo
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                settings["image_url"] = filename  # Guarda o nome da imagem, não o caminho completo
        
        # Ajuste das configurações de imagem
        for key in settings.keys():
            if key in request.form and key != "image_url":
                settings[key] = float(request.form[key])

    return render_template("index.html", **settings)

if __name__ == "__main__":
    app.run(debug=True)
