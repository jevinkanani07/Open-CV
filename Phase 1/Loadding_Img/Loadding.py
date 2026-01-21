import cv2

image = cv2.imread("Rose img.jpg")

if image is None:
    print("Image Is Not Found")
else:
    print("image Is Found Sucssesfully")