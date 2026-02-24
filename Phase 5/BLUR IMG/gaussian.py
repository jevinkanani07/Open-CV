import cv2

image = cv2.imread("Jevin.jpg")

blur = cv2.GaussianBlur(image,(21,21),10)

cv2.imshow("Original",image)
cv2.imshow("Blur_img",blur)

cv2.imwrite("Save_img.jpg",blur)
cv2.waitkey(0)
cv2.destroyAllWindows()