from flask import Flask, render_template, request
from ultralytics import YOLO
import cv2
import os

app = Flask(__name__)

# Folders
UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load YOLO model once
model = YOLO("best.pt")

@app.route("/", methods=["GET", "POST"])
def index():

    result_filename = None

    if request.method == "POST":

        # Check if file uploaded
        if "image" not in request.files:
            return render_template("index.html")

        file = request.files["image"]

        if file.filename == "":
            return render_template("index.html")

        # Save uploaded image
        image_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        file.save(image_path)

        # Run YOLO detection
        results = model(image_path)

        # Draw bounding boxes
        plotted_image = results[0].plot()

        # Save result image
        result_filename = "result_" + file.filename

        result_path = os.path.join(
            RESULT_FOLDER,
            result_filename
        )

        cv2.imwrite(result_path, plotted_image)

        print("Result saved:", result_path)

    return render_template(
        "index.html",
        result_filename=result_filename
    )

if __name__ == "__main__":
    app.run(debug=True)