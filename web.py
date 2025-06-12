from flask import Flask, request, render_template
from modelo import prediction
import base64
from io import BytesIO
from PIL import Image


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    image_data = None
    resultado = None  # ← Aseguramos que esté definida siempre

    if request.method == "POST":
        file = request.files.get("image")
        if file:
            image = Image.open(file.stream).convert("RGB")

            resultado = prediction(image)

            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode()
            image_data = f"data:image/png;base64,{img_base64}"

    return render_template("home.html", image_data=image_data, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)