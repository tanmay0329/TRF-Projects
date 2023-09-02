import cv2

width = 400
height = 300

win = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

for x in range(width):
    for y in range(height):
        new_pixel = image.Pixel(255, 0, 0)
        img.set_pixel(x, y, new_pixel)
    img.draw(win)