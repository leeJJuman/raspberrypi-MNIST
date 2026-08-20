# Raspberry Pi Digit Recognition

Raspberry Pi Camera를 이용하여 실시간 영상을 입력받고
TensorFlow Lite 모델로 손글씨 숫자를 인식합니다.

# Demo

* YouTube: [(https://www.youtube.com/watch?v=RGFJBGFC2qQ)]

# Environment

## Hardware

* Raspberry Pi 4
* Raspberry Pi Camera

## Software

* Python
* TensorFlow
* OpenCV
* Picamera2
* NumPy

# Recognition Pipeline

* Camera Capture
* HSV Masking
* Largest Contour Detection
* Square Padding
* 28 x 28 Resize
* TensorFlow Lite Inference
* Digit Prediction

# Features

* 실시간 카메라 입력
* HSV 기반 숫자 영역 추출
* 가장 큰 숫자 윤곽 선택
* 28 x 28 전처리
* TensorFlow Lite 추론
* 예측 숫자와 신뢰도 표시

# Files

* camera_mnist.py
* ../train/mnist_model.tflite

# Run

* Python 가상환경 활성화
* TensorFlow와 OpenCV 설치
* camera_mnist.py 실행
* 카메라 앞의 숫자 인식 확인

# Future Improvements

* 다양한 조명 환경에서의 인식 개선
* 숫자 영역 자동 보정
* 여러 숫자 동시 인식
* 추론 속도 최적화
