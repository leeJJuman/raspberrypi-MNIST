# MNIST Raspberry Pi Digit Recognition

MNIST 데이터셋을 이용하여 숫자 인식 모델을 학습하고
학습된 TensorFlow Lite 모델을 Raspberry Pi로 전송하여
Raspberry Pi Camera를 통해 숫자를 인식하는 프로젝트입니다.

Windows에서 모델을 학습한 후 PowerShell을 이용하여 Raspberry Pi로 파일을 전송하고,
Raspberry Pi 가상환경에서 TensorFlow를 구성한 뒤 카메라 기반 Digit Recognition을 구현했습니다.

# Environment

## Hardware

* Raspberry Pi 4
* Raspberry Pi Camera

## Software

* Python
* Jupyter Notebook
* TensorFlow
* TensorFlow Lite
* OpenCV
* Picamera2
* NumPy
* Windows PowerShell

# Project Structure

* train
* MNIST_Training.ipynb
* mnist_model.tflite
* README.md
* raspberrypi
* camera_mnist.py

# Practice

## 01. MNIST Model Training

MNIST 데이터셋을 이용하여 숫자 인식 모델을 학습합니다.

* MNIST Dataset
* Data Preprocessing
* Dense Layer
* Model Training
* Model Evaluation
* TensorFlow Lite Conversion

## 02. Raspberry Pi Setup

Windows PowerShell을 이용하여 학습된 모델과 코드를 Raspberry Pi로 전송합니다.

Raspberry Pi에서 Python 가상환경을 생성하고 TensorFlow를 설치하여
학습된 모델을 실행할 수 있는 환경을 구성합니다.

* PowerShell
* SCP
* Raspberry Pi
* Python Virtual Environment
* TensorFlow

## 03. Digit Recognition

Raspberry Pi Camera와 Picamera2를 이용하여 영상을 입력받고
TensorFlow Lite 모델을 이용하여 숫자를 인식합니다.

* Camera Capture
* Image Preprocessing
* OpenCV
* TensorFlow Lite
* Digit Recognition

# Learning Process

* MNIST Dataset
* Data Preprocessing
* Neural Network
* Model Training
* TensorFlow Lite
* PowerShell
* Raspberry Pi
* Python Virtual Environment
* TensorFlow
* Picamera2
* OpenCV
* Digit Recognition

# Future Improvements

* 숫자 영역 자동 검출
* 이미지 전처리 개선
* 실제 카메라 환경에서의 인식 정확도 향상
* 여러 숫자 인식
* Raspberry Pi 추론 속도 개선
