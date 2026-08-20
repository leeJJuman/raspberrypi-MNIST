# MNIST Model Training

MNIST 데이터셋을 이용하여 숫자 인식 모델을 학습하고
학습된 Keras 모델을 TensorFlow Lite 형식으로 변환합니다.

# Environment

## Software

* Python
* Jupyter Notebook
* TensorFlow
* NumPy
* Matplotlib
* Scikit-learn
* Seaborn

# Practice

## 01. MNIST Dataset

MNIST 데이터셋을 불러오고 모델 학습을 위한 데이터를 전처리합니다.

* MNIST Dataset
* Training Data
* Test Data
* Image Normalization
* One-hot Encoding

## 02. Model Training

28 x 28 크기의 MNIST 이미지를 Flatten하여
Dense Layer 기반의 숫자 분류 모델을 학습합니다.

* Flatten
* Dense Layer
* ReLU
* Softmax
* Adam Optimizer
* Model Training

## 03. Model Evaluation

테스트 데이터를 이용하여 학습된 모델의 성능을 평가합니다.

* Loss
* Accuracy
* Confusion Matrix
* Class Accuracy

## 04. TensorFlow Lite

학습된 Keras 모델을 TensorFlow Lite 형식으로 변환하여
Raspberry Pi에서 사용할 수 있도록 저장합니다.

* Keras Model
* TensorFlow Lite
* Model Conversion
* TFLite Model

# Model

* Input: 28 x 28 Grayscale Image
* Hidden Layer: Dense 100
* Activation: ReLU
* Output Layer: Dense 10
* Output Activation: Softmax
* Optimizer: Adam
* Epochs: 30

# Result

* Training Accuracy: 99.92%
* Validation Accuracy: 97.21%
* Test Accuracy: 97.56%

# Files

* MNIST_Training.ipynb
* mnist_model.tflite
