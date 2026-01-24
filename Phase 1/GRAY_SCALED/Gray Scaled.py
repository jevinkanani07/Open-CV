import cv2

path = input("Please Enter Your Img Path :- ")
image = cv2.imread(path)

if image is None:
    print(" Your Enter Path is InValid")
    exit()
else:
    print("Your Enter Path is Valid")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

choice = input("Do you want to SHOW or AVE your image").lower()

if choice == "show":
    cv2.imshow("Grayscale Image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif choice == "save":
    path2 = input("Enter Your Path where you save img")
    if path2 is not None:
        cv2.imwrite(path2,gray)

    else:
        print("Your path Is not Found")

else:
    print("Image could be not found")

