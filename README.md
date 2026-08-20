# MNIST Raspberry Pi Digit Recognition

MNIST 데이터셋을 이용하여 숫자 인식 모델을 학습하고
Raspberry Pi Camera를 활용하여 실시간으로 숫자를 인식하는 프로젝트입니다.

Jupyter Notebook을 이용한 모델 학습부터
Windows PowerShell을 통한 Raspberry Pi 파일 전송,
Raspberry Pi 가상환경 구성 및 TensorFlow 설치,
카메라 기반 Digit Recognition까지 구현했습니다.

## Environment

### Hardware

* Raspberry Pi 4
* Raspberry Pi Camera

### Software

* Python
* Jupyter Notebook
* TensorFlow
* OpenCV
* Picamera2
* NumPy
* Windows PowerShell

## Project Structure

* train
* MNIST_Training.ipynb
* raspberrypi
* camera_mnist.py
* README.md

## Practice

### 01. MNIST Model Training

MNIST 데이터셋을 이용하여 숫자 인식 모델을 학습합니다.

* MNIST Dataset
* Data Preprocessing
* CNN Model
* Model Training
* Model Evaluation

### 02. Raspberry Pi Setup

Windows PowerShell을 이용하여 학습된 모델을 Raspberry Pi로 전송하고
Raspberry Pi 가상환경에서 TensorFlow를 설치합니다.

* PowerShell
* SCP
* Python Virtual Environment
* TensorFlow

### 03. Digit Recognition

Raspberry Pi Camera와 Picamera2를 이용하여 영상을 입력받고
학습된 모델을 이용하여 숫자를 인식합니다.

* Camera Capture
* Image Preprocessing
* OpenCV
* TensorFlow Inference
* Digit Recognition

## Learning Process

* MNIST
* CNN
* TensorFlow
* Raspberry Pi
* Picamera2
* OpenCV
* Image Processing
* Digit Recognition

## Future Improvements

* 숫자 영역 자동 검출
* 이미지 전처리 개선
* 실제 카메라 환경에서의 인식 정확도 향상
* 여러 숫자 인식
* Raspberry Pi 추론 속도 개선
