import cv2
import drawsvg as draw


input_file = "images/moon.png"
DIFFERENCE_THRESHOLD = 1
convert_transparent_to_color = [255, 255, 255, 100]
OUTPUT_SCALE = 1


# ######################################################


image = cv2.imread(input_file, cv2.IMREAD_UNCHANGED)

image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=convert_transparent_to_color)

image[image[:, :, 3] == 0] = convert_transparent_to_color

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).tolist()

d = draw.Drawing(len(image[0]), len(image))

for r, row in enumerate(image):
    for c, column in enumerate(row):
        if r < len(image) - 1 and c < len(image[0]) - 1:
            if abs(image[r][c] - image[r+1][c]) >= DIFFERENCE_THRESHOLD:
                d.append(draw.Lines(c, r + 1, c + 1, r + 1, stroke_width=len(image) * 0.005, stroke="black"))
            if abs(image[r][c+1] - image[r][c]) >= DIFFERENCE_THRESHOLD:
                d.append(draw.Lines(c + 1, r, c + 1, r + 1, stroke_width=len(image) * 0.005, stroke="black"))

d.set_pixel_scale(OUTPUT_SCALE)

d.save_svg(f"{input_file}_{OUTPUT_SCALE}x.svg")
