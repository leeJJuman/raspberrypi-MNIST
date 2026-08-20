from picamera2 import Picamera2
import cv2
import numpy as np
import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="/home/dlwjdwnman/MNIST/mnist_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_index = input_details[0]['index']
output_index = output_details[0]['index']

def main():
    height = 480
    width = 640
    cam = Picamera2()
    cam.configure(cam.create_video_configuration(main={'format': 'XRGB8888', 'size': (width, height)}))
    cam.start()

    try:
        while True:
            frame = cam.capture_array()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            lower = np.array([0, 0, 0])
            upper = np.array([180, 255, 80])

            mask = cv2.inRange(hsv, lower, upper)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            best_contour = None
            max_area = 0

            for contour in contours:
                area = cv2.contourArea(contour)

                if area < 500:
                    continue

                x, y, w, h = cv2.boundingRect(contour)

                if w < 20 or h < 20:
                    continue

                if w > 300 or h > 300:
                    continue

                if area > max_area:
                    max_area = area
                    best_contour = contour

            if best_contour is not None:
                x, y, w, h = cv2.boundingRect(best_contour)

                pad = int(max(w, h) * 0.2)

                x1 = max(0, x - pad)
                y1 = max(0, y - pad)
                x2 = min(mask.shape[1], x + w + pad)
                y2 = min(mask.shape[0], y + h + pad)

                digit = mask[y1:y2, x1:x2]

                h_digit, w_digit = digit.shape
                size = max(w_digit, h_digit)

                canvas = np.zeros((size, size), dtype=np.uint8)

                x_offset = (size - w_digit) // 2
                y_offset = (size - h_digit) // 2

                canvas[y_offset:y_offset+h_digit, x_offset:x_offset+w_digit] = digit

                digit28 = cv2.resize(canvas, (28, 28), interpolation=cv2.INTER_AREA)

                input_data = digit28.astype(np.float32) / 255.0
                input_data = input_data.reshape(1, 28, 28)

                interpreter.set_tensor(input_index, input_data)
                interpreter.invoke()

                output = interpreter.get_tensor(output_index)

                prediction = np.argmax(output)
                confidence = np.max(output)

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(frame, f'Pred : {prediction}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3)
                cv2.putText(frame, f'conf : {confidence:.2f}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3)

                cv2.imshow('digit28', digit28)
                cv2.imshow('frame', frame)
                cv2.imshow('mask', mask)

            key = cv2.waitKey(1) & 0xFF

            if key == 27 or key == ord('q'):
                break

    finally:
        cam.stop()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
