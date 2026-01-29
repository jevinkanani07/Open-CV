import cv2

image = cv2.imread("FILPPED\Cartoon_Human.jpg")

if image is None:
    print("image is not found")
else:
    flipped_horizontal = cv2.flip(image,1)
    flipped_vertical = cv2.flip(image,0)
    flipped_both = cv2.flip(image,-1)

    cv2.imshow("Original",image)
    cv2.imshow("flipped horizontal",flipped_horizontal)
    cv2.imshow("flipped vertical",flipped_vertical)
    cv2.imshow("flipped_both",flipped_both)

    cv2.imwrite("FILPPED\flipped_horizontal.jpg",flipped_horizontal)
    cv2.imwrite("FILPPED\flipped_vertical.jpg",flipped_vertical)
    cv2.imwrite("FILPPED\flipped_both.jpg",flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()