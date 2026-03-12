This code is designed to take a frame every second (live) and apply the cartoon filter or effect on it.
The camera of your laptop/PC opens due to the line cap = cv2.VideoCapture(0), where zero means the default camera of your system.
If you have multiple cameras, you can change the number to 1, 2, etc., to use a different camera.

When you want to close your camera frame, just press 'q'.

To clarify: the cartoon effect is created by combining the smoothed, color-quantized image with the inverted edges.
So basically, it’s a mix of color enhancement, smoothing, color simplification, and edge highlighting
(cv2.equalizeHist, cv2.bilateralFilter, cv2.kmeans, cv2.Canny).


<img width="1349" height="528" alt="Cartoni2" src="https://github.com/user-attachments/assets/ec60dd4f-6f63-4c8a-afe1-ab3b78333c84" />




<img width="765" height="395" alt="Cartoni" src="https://github.com/user-attachments/assets/2ae2736c-e229-4fba-b771-3106afcc3347" />






