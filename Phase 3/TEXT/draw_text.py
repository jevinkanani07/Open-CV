import cv2

image = cv2.imread("Cartoon_Human.jpg")

if image is None:
    print("image is not found")
else:
    print("sucsses! image is found")

    cv2.putText(image,"Hello! I'AM Jevin",(50,300),cv2.FONT_HERSHEY_SIMPLEX,1.2 ,(250,0,0),2)

    cv2.imshow("Originai",image)
    cv2.imshow("Add A Text On Img",image)

    cv2.imwrite("drow_img.jpg",image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()