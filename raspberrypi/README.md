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

# Result

* Raspberry Pi Camera를 이용한 실시간 숫자 인식 구현
* HSV 마스킹을 이용하여 숫자 영역 검출
* 검출된 숫자 영역을 28 x 28 크기로 변환 후 추론
* 인식 결과와 confidence를 실시간으로 표시
* 대부분의 숫자를 정상적으로 인식
* 숫자 7과 9에서 상대적으로 인식이 불안정한 경우가 확인됨
* HSV의 V 범위에 따라 숫자 영역이 일부 손실되어 마스크가 깨지는 경우가 확인됨
* 반복적인 입력을 통해 최종적으로 숫자를 정상적으로 인식하는 것을 확인

# Limitations

* HSV의 V 범위에 따라 숫자 영역 검출 결과가 달라질 수 있음
* 조명이나 숫자의 밝기에 따라 마스크 영역이 일부 손실될 수 있음
* 숫자 영역이 깨지는 경우 28 x 28 변환 과정에서 정보가 추가로 손실될 수 있음
* 7과 9의 인식이 다른 숫자보다 상대적으로 불안정함

# Future Improvements

* HSV V 범위 최적화
* 숫자 영역 마스킹 개선
* 조명 변화에 강한 전처리 적용
* 숫자 영역 자동 보정
* 7과 9의 인식 정확도 개선
* 여러 숫자 인식
* Raspberry Pi 추론 속도 개선

