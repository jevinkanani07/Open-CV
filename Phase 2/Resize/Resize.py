import cv2

image = cv2.imread("Cartoon_Human.jpg")

if image is None:
    print("image is not found")
else:
    print("image loaded")

    resized = cv2.resize(image,(300,300))

    cv2.imshow("Original",image)
    cv2.imshow("Resize image",resized)

    cv2.imwrite("Resize_image.jpg",resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows