import cv2
import numpy as np
from rgb2ansi import rgb2short_fast
from sty import fg


def renderImg(img):
    # img = cv2.imread("deadpool.jpg")
    width, height, _ = img.shape
    aspectRatio = height / width
    newWidth = 120
    newHeight = int(newWidth * aspectRatio * 0.25)
    img = cv2.resize(img, (newWidth, newHeight))

    colorCodes = []
    for row in img:
        colorCodes.append([rgb2short_fast(pixel) for pixel in row])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    chars = ["B", "S", "#", "&", "@", "$", "%", "*", "+", "!", ":", "."]
    newImg = []
    for rowIndex in range(len(img)):
        temp = []
        for cellIndex in range(len(img[rowIndex])):
            print(
                fg(colorCodes[rowIndex][cellIndex])
                + chars[img[rowIndex][cellIndex] // 25],
                end="",
            )
            temp.append(
                fg(colorCodes[rowIndex][cellIndex])
                + chars[img[rowIndex][cellIndex] // 25]
            )
        newImg.append("".join(temp))
        print()
    import sys

    with open("test.txt", "w") as fl:
        fl.writelines(newImg)

    CURSOR_ONE_UP = "\033[A"
    for i in range(len(img)):
        sys.stdout.write(CURSOR_ONE_UP)


def main():
    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        renderImg(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
