import cv2

image = cv2.imread("ROTATION\Cartoon_Human.jpg")

if image is None:
    print("image is not found")
else:
    (w,h) = image.shape[:2]
    center = (w//2 , h//2)

    M = cv2.getRotationMatrix2D(center, 90,1.0)
    rotated = cv2.warpAffine(image, M, (w,h))

    cv2.imshow("Original",image)
    cv2.imshow("Rotated image",rotated)

    cv2.imwrite("ROTATION\Rotated_image.jpg",rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()