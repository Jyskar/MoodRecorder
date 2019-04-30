from PIL import Image, ImageDraw
import InOut


def draw_grid():
    y_start = 0
    y_end = image.height

    for x in range(0, image.width, 315):
        lin = ((x, y_start), (x, y_end))
        draw.line(lin, fill=0, width=10)

    for x in range(0, image.width, 45):
        lin = ((x, y_start), (x, y_end))
        draw.line(lin, fill=0, width=3)
    x_start = 0
    x_end = image.width

    for y in range(0, image.height, 180):
        lin = ((x_start, y), (x_end, y))
        draw.line(lin, fill=0, width=10)

    for y in range(0, image.height, 45):
        lin = ((x_start, y), (x_end, y))
        draw.line(lin, fill=0, width=3)


if __name__ == '__main__':

    days = InOut.read_from_file("test.txt")
    image = Image.new('RGB', [945, 720], color=(255, 255, 255))

    # Draw some lines
    draw = ImageDraw.Draw(image)

    xi = 2
    yi = 2
    xf = 43
    yf = 43
    for i in range(0, 17):
        for z in range(0, 21):
            if (i*17)+z < len(days):
                draw.rectangle([(xi, yi), (xf, yf)], days[(i*17)+z].color)
            xi += 45
            xf += 45
        yi += 45
        yf += 45
        xi = 2
        xf = 43

    draw_grid()
    image.show()
