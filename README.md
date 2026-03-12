This code is designed to take a frame every second (live) and apply the cartoon filter or effect on it.
The camera of your laptop/PC opens due to the line cap = cv2.VideoCapture(0), where zero means the default camera of your system.
If you have multiple cameras, you can change the number to 1, 2, etc., to use a different camera.

When you want to close your camera frame, just press 'q'.

To clarify: the cartoon effect is created by combining the smoothed, color-quantized image with the inverted edges.
So basically, it’s a mix of color enhancement, smoothing, color simplification, and edge highlighting
(cv2.equalizeHist, cv2.bilateralFilter, cv2.kmeans, cv2.Canny).

This is a simple Python project that uses OpenCV to convert live webcam video into a cartoon-style image.

First, the program imports the required libraries:

import cv2
import numpy as np

Then a function called color_quant(image, k=8) is created. This function reduces the number of colors in the image using K-Means clustering, which helps make the image look simpler and more cartoon-like.

def color_quant(image, k=8):
    Z = image.reshape((-1,3)).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quant = centers[labels.flatten()].reshape(image.shape)
    return quant

After that, the webcam is started using:

cap = cv2.VideoCapture(0)

Inside a loop, the program reads frames from the camera:

ret, frame = cap.read()

Each frame is resized to make the processing faster:

frame = cv2.resize(frame, (640,480))

Then the program improves the contrast by splitting the color channels, applying histogram equalization, and merging them again:

b,g,r = cv2.split(frame)

frame_eq = cv2.merge([
    cv2.equalizeHist(b),
    cv2.equalizeHist(g),
    cv2.equalizeHist(r)
])

Next, the image is smoothed using a bilateral filter to reduce noise while keeping edges clear:

smooth = cv2.bilateralFilter(frame_eq, 9, 75, 75)

After smoothing, the number of colors is reduced using the color quantization function:

cartoon = color_quant(smooth, k=8)

To create the cartoon edges, the image is converted to grayscale and edges are detected using the Canny edge detector:

gray = cv2.cvtColor(smooth, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 80, 160)

The edges are then inverted and converted back to a 3-channel image:

edges_inv = cv2.bitwise_not(edges)
edges_inv = cv2.cvtColor(edges_inv, cv2.COLOR_GRAY2BGR)

Finally, the edges are combined with the simplified colors to create the cartoon effect:

output = cv2.bitwise_and(cartoon, edges_inv)

The result is displayed in a window:

cv2.imshow("Cartoon", output)

The program keeps running until the user presses Q, then the camera is released and all windows are closed.

cap.release()
cv2.destroyAllWindows()
