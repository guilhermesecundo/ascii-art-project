from PIL import Image
import numpy as np

class ASCIIConverter:
    def __init__(self, charset="@%#*+=-:. "):
        self.charset = charset

    def pixel_to_ascii(self, pixel_value):
        num_chars = len(self.charset)
        return self.charset[int(pixel_value / 256 * num_chars)]

    def image_to_ascii(self, image_path):
        image = Image.open(image_path)
        pixel_matrix = np.array(image)

        ascii_art = ""
        for row in pixel_matrix:
            line = "".join(self.pixel_to_ascii(pixel) for pixel in row)
            ascii_art += line + "\n"

        return ascii_art
    
    def save_ascii_art(self, ascii_art, filename):
        with open(filename, 'w') as file:
            file.write(ascii_art)


if __name__ == "__main__":
    converter = ASCIIConverter()
    ascii_result = converter.image_to_ascii("output.jpg")
    converter.save_ascii_art(ascii_result, "output.txt")
    print("ASCII successfully saved to output.txt !")