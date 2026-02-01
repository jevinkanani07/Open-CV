import cv2

image = cv2.imread("Cartoon_Human.jpg")

if image is None:
    print("image is not found")
else:
    print("sucsses! image is found")

    cv2.circle(image,(300,220),120, (250,0,0)  , 4)

    cv2.imshow("Originai",image)
    cv2.imshow("drow Circle",image)

    cv2.imwrite("drow_img.jpg",image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()