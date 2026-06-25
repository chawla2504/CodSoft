# Face Detection System

## Overview

This project is a real-time Face Detection System developed using Python and OpenCV. The system detects human faces from a live webcam feed and highlights them using bounding boxes.

## Features

- Real-time face detection
- Multiple face detection
- Face counting
- Bounding box visualization
- Face labeling
- Webcam integration

## Technologies Used

- Python
- OpenCV
- Haar Cascade Classifier

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python face_detection.py
```

## How It Works

The application captures video frames from a webcam and converts them to grayscale. OpenCV's Haar Cascade Classifier scans each frame to identify facial features and returns face coordinates. Detected faces are highlighted using rectangles and labels.

