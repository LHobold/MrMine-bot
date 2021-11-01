from PIL import Image, ImageChops
from mss import mss, tools


def print_screen(top, left, width, height, name):
    with mss() as sct:
        monitor = {"top": top, "left": left, "width": width, "height": height}
        output = ("../images/cap/%s-cap.png" % name).format(**monitor)
        sct_img = sct.grab(monitor)
        tools.to_png(sct_img.rgb, sct_img.size, output=output)


def images_are_similar(img1, img2, sumSquares):
    diff = ImageChops.difference(img1, img2).histogram()
    sq = (value * (i % 256) ** 2 for i, value in enumerate(diff))
    sum_squares = sum(sq)
    print(sum_squares)
    return sum_squares < sumSquares


print_screen(305, 580, 750, 600, 'cave')

cap = Image.open('../images/cap/cave-cap.png')
src = Image.open('../images/src/cave-src.png')

print(images_are_similar(cap, src, 1000000000))
