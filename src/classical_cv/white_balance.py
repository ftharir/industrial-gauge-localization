import cv2
import numpy as np

# تابع White Balance
def simple_white_balance(img):
    result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    avg_a = np.mean(result[:, :, 1])
    avg_b = np.mean(result[:, :, 2])
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
    return cv2.cvtColor(result, cv2.COLOR_LAB2BGR)

# خواندن تصویر
image = cv2.imread('image.jpg')
"""
# اعمال White Balance
wb_image = simple_white_balance(image)

# نمایش تصویر
cv2.imshow('Original Image', image)
cv2.imshow('White Balanced Image', wb_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""