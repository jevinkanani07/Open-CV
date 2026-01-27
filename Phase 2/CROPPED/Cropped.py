import cv2

image = cv2.imread("Cartoon_Human.jpg")

if image is not None:
    cropped = image[100:1000, 50:1500]

    cv2.imshow("ORIGINAL",image)
    cv2.imshow("CROPPED IMAGE",cropped)

    cv2.imwrite("Cropped_img.jpg",cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("image not found")
