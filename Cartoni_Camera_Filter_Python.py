import cv2
import numpy as np

def color_quant(image, k=8):
    Z = image.reshape((-1,3)).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quant = centers[labels.flatten()].reshape(image.shape)
    return quant

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera error")
        break

    frame = cv2.resize(frame, (640,480))

   
    b,g,r = cv2.split(frame)
    frame_eq = cv2.merge([
        cv2.equalizeHist(b),
        cv2.equalizeHist(g),
        cv2.equalizeHist(r)
    ])

   
    smooth = cv2.bilateralFilter(frame_eq, 9, 75, 75)

   
    cartoon = color_quant(smooth, k=8)

   
    gray = cv2.cvtColor(smooth, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 160)

   
    edges_inv = cv2.bitwise_not(edges)
    edges_inv = cv2.cvtColor(edges_inv, cv2.COLOR_GRAY2BGR)

    output = cv2.bitwise_and(cartoon, edges_inv)

    cv2.imshow("Cartoon", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
