import cv2

image = cv2.imread("blur_img.jpg")

blur = cv2.medianBlur(image,21)

cv2.imshow("Original",image)
cv2.imshow("Blur_img",blur)

cv2.imwrite("Save_img.jpg",blur)
cv2.waitkey(0)
cv2.destroyAllWindows()