# License Plate Detection using YOLOv8, OpenCV & Flask

## Overview

This project is a web-based License Plate Detection System built using **YOLOv8**, **OpenCV**, and **Flask**. The application detects vehicle license plates from uploaded images and displays the detected plate region with bounding boxes.

The custom YOLOv8 model is trained on a license plate dataset containing a single class:

* **Licence-Plate**

---

## Features

* 🚗 Automatic license plate detection
* 🎯 Custom-trained YOLOv8 model
* 📷 Image upload through Flask web interface
* 🖼️ Bounding box visualization using OpenCV
* ⚡ Fast and accurate detection
* 🌐 Easy-to-use web application

---

## Dataset Configuration

```yaml
path: ../Licence late Detection.yolov8
train: train/images
val: valid/images

nc: 1

names:
  - Licence-Plate
```

---

## Tech Stack

* Python 3.x
* YOLOv8 (Ultralytics)
* OpenCV
* Flask
* NumPy

---

## Project Structure

```text
License-Plate-Detection/
│
├── app.py
├── best.pt
├── static/
│   ├── uploads/
│   └── results/
│
├── templates/
│   └── index.html
│
├── dataset/
│   ├── train/
│   └── valid/
│
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/license-plate-detection.git

cd license-plate-detection
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Model Training

Install Ultralytics:

```bash
pip install ultralytics
```

Train the model:

```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640
```

After training, the best model will be saved as:

```text
runs/detect/train/weights/best.pt
```

Copy the `best.pt` file to the project root directory.

---

## Running the Flask Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Upload an image containing a vehicle, and the system will detect and highlight the license plate.

---

## Detection Workflow

1. User uploads an image.
2. Flask receives the image.
3. YOLOv8 model performs license plate detection.
4. OpenCV draws bounding boxes around detected plates.
5. Processed image is displayed to the user.

---

## Sample Output

```text
Input Image
     ↓
YOLOv8 Detection
     ↓
Bounding Box on License Plate
     ↓
Output Image Displayed
```

---

## Requirements

```text
flask
opencv-python
ultralytics
numpy
pillow
```

Install manually:

```bash
pip install flask opencv-python ultralytics numpy pillow
```

---

## Future Improvements

* License plate character recognition (OCR)
* Real-time webcam detection
* Video stream processing
* Vehicle tracking integration
* Database logging of detected plates

---

## Results

The custom YOLOv8 model successfully detects license plates in vehicle images with high accuracy and fast inference speed, making it suitable for parking management, traffic monitoring, and vehicle identification applications.

---
