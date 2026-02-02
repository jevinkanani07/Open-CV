import cv2

image = cv2.imread("Cartoon_Human.jpg")

if image is None:
    print("image is not found")
else:
    print("sucsses! image is found")

    plt1= (50,100)
    plt2 = (100,300)

    color = (255,0,0)
    think = 3

    cv2.line(image,plt1, plt2 , color , think)

    cv2.imshow("Originai",image)
    cv2.imshow("drow line",image)

    cv2.imwrite("drow_img.jpg",image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
