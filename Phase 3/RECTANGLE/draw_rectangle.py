import cv2

image = cv2.imread("Cartoon_Human.jpg")

if image is None:
    print("image is not found")
else:
    print("sucsses! image is found")

    plt1= (50,50)
    plt2 = (200,250)

    color = (0,0,255)
    think = 3

    cv2.rectangle(image,plt1, plt2 , color , think)

    cv2.imshow("Originai",image)
    cv2.imshow("drow rectangle",image)

    cv2.imwrite("drow_img.jpg",image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()