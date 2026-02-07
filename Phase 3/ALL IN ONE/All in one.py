import cv2
import os

path = input("Enter image full path: ")

image = cv2.imread(path)

if image is None:
    print("Image path is INVALID")
    exit()
else:
    print(" Image path is VALID")

print("\nChoose what you want to add:")
print("1. line")
print("2. rectangle")
print("3. circle")
print("4. text")

choice = input("Enter option (line/rectangle/circle/text): ").lower()

def get_color():
    print("Enter color (B G R):")
    b = int(input("B: "))
    g = int(input("G: "))
    r = int(input("R: "))
    return (b, g, r)

if choice == "line":
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    thickness = int(input("Thickness: "))
    color = get_color()

    cv2.line(image, (x1, y1), (x2, y2), color, thickness)

elif choice == "rectangle":
    x1 = int(input("Top-left x: "))
    y1 = int(input("Top-left y: "))
    x2 = int(input("Bottom-right x: "))
    y2 = int(input("Bottom-right y: "))
    thickness = int(input("Thickness: "))
    color = get_color()

    cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)

elif choice == "circle":
    x = int(input("Center x: "))
    y = int(input("Center y: "))
    radius = int(input("Radius: "))
    thickness = int(input("Thickness: "))
    color = get_color()

    cv2.circle(image, (x, y), radius, color, thickness)

elif choice == "text":
    text = input("Enter text: ")
    x = int(input("Text x position: "))
    y = int(input("Text y position: "))
    font_scale = float(input("Font scale (e.g. 1.0): "))
    thickness = int(input("Thickness: "))
    color = get_color()

    print("\nFont options:")
    print("1. SIMPLEX")
    print("2. PLAIN")
    print("3. DUPLEX")
    print("4. COMPLEX")

    font_choice = int(input("Choose font number: "))

    fonts = {
        1: cv2.FONT_HERSHEY_SIMPLEX,
        2: cv2.FONT_HERSHEY_PLAIN,
        3: cv2.FONT_HERSHEY_DUPLEX,
        4: cv2.FONT_HERSHEY_COMPLEX
    }

    font = fonts.get(font_choice, cv2.FONT_HERSHEY_SIMPLEX)

    cv2.putText(image, text, (x, y), font, font_scale, color, thickness)

else:
    print(" Invalid option")
    exit()

cv2.imshow("Final Image", image)

save_path = os.path.join(os.path.dirname(path), "edited_image.jpg")
cv2.imwrite(save_path, image)

print(f"\n Image saved at:\n{save_path}")

cv2.waitKey(0)
cv2.destroyAllWindows()