from PIL import Image, ImageChops
from mss import mss, tools
from config import statusPositions


def print_screen(top, left, width, height, name):
    with mss() as sct:
        monitor = {"top": top, "left": left, "width": width, "height": height}
        output = ("./images/cap/%s-cap.png" % name).format(**monitor)
        sct_img = sct.grab(monitor)
        tools.to_png(sct_img.rgb, sct_img.size, output=output)


def images_are_similar(img1, img2, sumSquares):
    diff = ImageChops.difference(img1, img2).histogram()
    sq = (value * (i % 256) ** 2 for i, value in enumerate(diff))
    sum_squares = sum(sq)
    return sum_squares < sumSquares


def check_screen_status(name):
    pos = [x for x in statusPositions if x["name"] == name][0]

    print_screen(pos["top"], pos["left"], pos["width"],
                 pos["height"], pos["name"])

    capImg = Image.open('./images/cap/%s-cap.png' % name)
    isStatus = images_are_similar(pos["srcImage"], capImg, pos["sumSquare"])
    return isStatus
