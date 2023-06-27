import cv2
import drawsvg as draw


input_file = "images/moon.png"
DIFFERENCE_THRESHOLD = 1
convert_transparent_to_color = [255, 255, 255, 100]
OUTPUT_SCALE = 1


def convert_image(input_path, transparent_color, threshold, scale):
    image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=transparent_color)
    image[image[:, :, 3] == 0] = transparent_color
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).tolist()

    d = draw.Drawing(len(image[0]), len(image))

    for r, row in enumerate(image):
        for c, column in enumerate(row):
            if r < len(image) - 1 and c < len(image[0]) - 1:
                if abs(image[r][c] - image[r+1][c]) >= threshold:
                    d.append(draw.Lines(c, r + 1, c + 1, r + 1, stroke_width=len(image) * 0.005, stroke="black"))
                if abs(image[r][c+1] - image[r][c]) >= threshold:
                    d.append(draw.Lines(c + 1, r, c + 1, r + 1, stroke_width=len(image) * 0.005, stroke="black"))

    d.set_pixel_scale(scale)
    d.save_svg(f"{input_path}_{scale}x.svg")
    return


if __name__ == "__main__":
    convert_image(input_path=input_file,
                  transparent_color=convert_transparent_to_color,
                  threshold=DIFFERENCE_THRESHOLD,
                  scale=OUTPUT_SCALE)
