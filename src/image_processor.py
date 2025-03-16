from PIL import Image   

# image_input = "example_image.png"

def load_image(image_input):
    image = Image.open(image_input)
    return image

def convert_to_grayscale(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def resize(image, max_width=300):
    width, height = image.size
    proportion = height / width  
    new_width = max_width
    new_height = int(proportion * new_width * 0.6)
    resized = image.resize((new_width, new_height))
    print(f"redimensionada para {new_width}x{new_height}.")
    return resized

def save_image(image, output_image):
    image.save(output_image)
    print(f"Imagem salva em {output_image}.")


def process_image(image_input, output_image, max_width=300):
    image = load_image(image_input)
    grayscale_image = convert_to_grayscale(image)
    resized_image = resize(grayscale_image, max_width)
    save_image(resized_image, output_image)


#teste
# process_image("example_image.png", "output.jpg", max_width=500)
